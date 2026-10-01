# GitHub Actions Workflows

This repository uses automated GitHub Actions workflows to manage site deployments, validate link integrity, automate faculty profile generation, link PRs to logistics tracking, and synchronize faculty registries across repositories.

## Deploy Jekyll Site (`deploy.yml`)
* **Trigger Events:** Push to `main` branch, manual dispatch (`workflow_dispatch`), or repository dispatch (`moledata-updated`).
Pulls the latest materials repository from `molevolworkshop/moledata`, builds an LFS asset index, caches LFS data, runs the site preparation script (`prep_build.sh`), and builds and deploys the Jekyll site to GitHub Pages. During preparation, materials are mounted under `/materials` and lab `README.md` files are converted into index pages with Jekyll frontmatter.

## Check Schedule Links (`check-schedule-links.yml`)
* **Trigger Events:** Push or Pull Request affecting `schedule.md`, script changes, or manual workflow dispatch.
Runs `scripts/check_schedule_links.py` against `schedule.md` to identify broken off-site URLs or missing local material files. Reports issues directly on commits and PRs without modifying content.

## Generate Faculty Placeholders (`generate-faculty-placeholders.yml`)
* **Trigger Events:** Push to `main` modifying `_data/faculty-registry.csv` or manual workflow dispatch.
Parses `_data/faculty-registry.csv` and checks the `_faculty/` directory. If any listed faculty member lacks a profile page, it duplicates `_faculty/faculty_template.md` to create a personalized placeholder page containing their name, title, and a direct edit link. Auto-commits new placeholders directly to `main`.

## Process Faculty Profile Issue (`process-faculty-profile.yml`)
* **Trigger Events:** Issues opened or edited with the `faculty-profile` label.
Parses issue forms submitted by faculty. Extracts bio, social handles, headshot, and affiliations to generate or update the markdown file in `_faculty/`. Opens an automated Pull Request targeting `main` with the changes and leaves a confirmation comment on the issue.

## Sync Faculty PR to Logistics Issue (`link-logistics-issue.yml`)
* **Trigger Events:** Pull Requests opened or updated (`synchronize`) modifying files in `_faculty/**`.
Scans modified faculty files to determine the instructor's name, then searches the `mole-logistics` repository for open issues labeled `needs-review` and `faculty-page`. When a matching issue is found, it updates the PR description to include a closing keyword (`Closes molevolworkshop/mole-logistics#<issue_number>`).

## Sync Faculty Dropdown to Website (`update-faculty-issue.yml`)
* **Trigger Events:** Push to `main` modifying `_data/faculty-registry.csv`.
Reads `_data/faculty-registry.csv` and updates the `faculty_select` dropdown options in `.github/ISSUE_TEMPLATE/faculty-profile.yml` via the GitHub API, ensuring issue form options stay aligned with the registry.

## Notify Repo on Faculty Update (`faculty-registry-ping.yml`)
* **Trigger Events:** Push to `main` modifying `_data/faculty-registry.csv`.
Generates an app token and dispatches a `faculty-registry-updated` event to the `moledata` repository using `repository_dispatch`, triggering cross-repository template synchronization.