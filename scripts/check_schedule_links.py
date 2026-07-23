#!/usr/bin/env python3
"""
check_schedule_links.py

Read the MOLE workshop schedule (schedule.md) and REPORT any broken links.
This script never edits anything -- it only reads and prints a report.

It checks three kinds of links found in schedule.md:

  1. Internal material links, e.g. {{ site.baseurl }}/materials/lectures/foo.pdf
     -> confirms the corresponding file actually exists in the `moledata` repo.
  2. Off-site links, e.g. https://figshare.com/... or a personal web page
     -> confirms the URL still resolves (is not dead).
  3. Malformed paths, e.g. a stray double slash //  -> flagged as a warning.

Other internal site links (like /faculty-heath/ or /labs/intro) are website
pages, not materials, so they are listed as "skipped" and not verified here.

USAGE
    python3 check_schedule_links.py [path-to-schedule.md]

    Defaults to ./schedule.md if no path is given.

    Options:
      --no-external   Skip pinging off-site URLs (only check moledata files).

EXIT CODE
    0  if no hard errors were found (warnings are allowed)
    1  if any material file is missing or any off-site link is definitively dead
       (so it can fail a GitHub Action).
"""

import json
import re
import sys
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Configuration -- edit here if the org/repo/branch ever changes.
# ---------------------------------------------------------------------------
MOLEDATA_OWNER = "molevolworkshop"
MOLEDATA_REPO = "moledata"
MOLEDATA_BRANCH = "main"

# On the website, moledata is copied into a folder called "materials/".
# So a link path "materials/lectures/x.pdf" maps to moledata "lectures/x.pdf".
MATERIALS_PREFIX = "materials/"

EXTERNAL_TIMEOUT = 10  # seconds
USER_AGENT = "mole-schedule-link-checker/1.0 (+https://github.com/molevolworkshop)"

# Markdown link:  [visible text](the-target)
# The target can contain spaces because of Liquid tags like {{ site.baseurl }},
# so capture everything up to the closing paren, then clean it up below.
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# Jekyll/Liquid variable such as {{ site.baseurl }} or {{site.baseurl}}
LIQUID_RE = re.compile(r"\{\{[^}]*\}\}")


def fetch_moledata_paths():
    """Return the set of every file path in the moledata repo."""
    url = (
        f"https://api.github.com/repos/{MOLEDATA_OWNER}/{MOLEDATA_REPO}"
        f"/git/trees/{MOLEDATA_BRANCH}?recursive=1"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    # Use a token if one is available (raises the API rate limit inside Actions).
    import os
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=EXTERNAL_TIMEOUT) as resp:
        data = json.load(resp)
    return {item["path"] for item in data.get("tree", []) if item.get("type") == "blob"}


def classify(raw_target):
    """
    Decide what kind of link this is and return (kind, cleaned_value, malformed).

    kind is one of: 'material', 'external', 'sitepage'
    """
    malformed = False
    target = LIQUID_RE.sub("", raw_target).strip()

    # Strip a leading slash left behind after removing the liquid variable.
    cleaned = target.lstrip("/")

    # Flag (and then tolerate) accidental double slashes in a path,
    # e.g. materials/lectures/machine_learning//file.pdf
    if "//" in cleaned and not cleaned.startswith("http"):
        malformed = True
        cleaned = re.sub(r"/{2,}", "/", cleaned)

    if target.startswith("http://") or target.startswith("https://"):
        return "external", target, malformed
    if cleaned.startswith(MATERIALS_PREFIX):
        return "material", cleaned, malformed
    return "sitepage", target, malformed


def material_to_moledata_path(cleaned):
    """materials/lectures/x.pdf  ->  lectures/x.pdf"""
    return cleaned[len(MATERIALS_PREFIX):]


def check_external(url):
    """Return (status, detail). status in {'ok','dead','warn'}."""
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(
                url, method=method, headers={"User-Agent": USER_AGENT}
            )
            with urllib.request.urlopen(req, timeout=EXTERNAL_TIMEOUT) as resp:
                if 200 <= resp.status < 400:
                    return "ok", f"HTTP {resp.status}"
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return "dead", f"HTTP {e.code}"
            if method == "GET":
                # Some servers dislike HEAD or block bots (403/405) -- can't be sure.
                return "warn", f"could not verify (HTTP {e.code})"
            # else: retry with GET
        except Exception as e:  # timeout, DNS failure, connection reset, etc.
            if method == "GET":
                return "warn", f"could not reach ({e.__class__.__name__})"
    return "warn", "could not verify"


def main():
    args = [a for a in sys.argv[1:]]
    check_external_links = "--no-external" not in args
    args = [a for a in args if a != "--no-external"]
    schedule_path = args[0] if args else "schedule.md"

    try:
        with open(schedule_path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"ERROR: could not find schedule file: {schedule_path}")
        return 1

    print(f"Checking links in {schedule_path} ...\n")

    try:
        moledata_paths = fetch_moledata_paths()
        print(f"Loaded {len(moledata_paths)} files from {MOLEDATA_REPO}.\n")
    except Exception as e:
        print(f"ERROR: could not load moledata file list: {e}")
        return 1

    missing_files = []      # internal material links with no matching file
    dead_links = []         # off-site links that are definitively dead
    warnings = []           # couldn't-verify + malformed paths
    skipped_pages = 0
    ok_count = 0

    for raw in LINK_RE.findall(text):
        kind, value, malformed = classify(raw)

        if malformed:
            warnings.append(f"malformed path (stray '//'): {raw}")

        if kind == "sitepage":
            skipped_pages += 1
            continue

        if kind == "material":
            mole_path = material_to_moledata_path(value)
            if mole_path in moledata_paths:
                ok_count += 1
            else:
                missing_files.append(f"{raw}  ->  expected moledata/{mole_path}")
            continue

        if kind == "external":
            if not check_external_links:
                skipped_pages += 1
                continue
            status, detail = check_external(value)
            if status == "ok":
                ok_count += 1
            elif status == "dead":
                dead_links.append(f"{value}  ({detail})")
            else:
                warnings.append(f"off-site link {value}  ({detail})")

    # ----------------------------------------------------------------- report
    print("=" * 70)
    print("LINK CHECK REPORT")
    print("=" * 70)
    print(f"  OK (verified)........ {ok_count}")
    print(f"  Missing files........ {len(missing_files)}")
    print(f"  Dead off-site links.. {len(dead_links)}")
    print(f"  Warnings............. {len(warnings)}")
    print(f"  Skipped site pages... {skipped_pages}")
    print()

    if missing_files:
        print("MISSING MATERIAL FILES (link points to a file not in moledata):")
        for m in missing_files:
            print(f"  - {m}")
        print()

    if dead_links:
        print("DEAD OFF-SITE LINKS:")
        for d in dead_links:
            print(f"  - {d}")
        print()

    if warnings:
        print("WARNINGS (worth a human glance, not necessarily broken):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if not (missing_files or dead_links or warnings):
        print("All links look good.\n")

    # Fail only on hard errors, so warnings don't block a rebuild.
    return 1 if (missing_files or dead_links) else 0


if __name__ == "__main__":
    sys.exit(main())
