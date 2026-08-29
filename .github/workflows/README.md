# GitHub Actions Workflows

This repository uses automated GitHub Actions workflows to manage site deployments, validate link integrity, and automate faculty profile generation and synchronization.

## Deploy Jekyll Site (`deploy.yml`)
- **Trigger Events:** Push to the `main` branch, manual dispatch, or repository dispatch (`moledata-updated`).
This action pulls the latest materials repository, caches LFS assets, runs the site preparation script, and builds and deploys the Jekyll site to GitHub Pages.
Importantly, files from moledata are dumped into `/materials`.
Further, `README.md` in labs are re-written as `index.md`; this adds some nessecary frontmatter for formatting and renders the page under the path of the folder that it sits in. 

## Check Schedule Links (`check-schedule-links.yml`)
- **Trigger Events:** Push or Pull Request affecting `schedule.md` or script changes, plus manual workflow dispatch.
Runs a link-checking script to report broken off-site links or missing material files in the schedule.

## Generate Faculty Placeholders (`generate-faculty-placeholders.yml`)
- **Trigger Events:** Push to `main` modifying `.github/ISSUE_TEMPLATE/faculty-profile.yml`.
Automatically scans the faculty registry and generates missing markdown placeholder pages in `_faculty/`.

## Process Faculty Profile (`process-faculty-profile.yml`)
- **Trigger Events:** Issues opened or edited with the `faculty-profile` label.
Parses faculty profile submission issues from the corresponding template. 
It generates or updates individual profile markdown files and updates registries as needed and opens an automated Pull Request.
If the main check issues were generated in `mole-logistics`, this action will link the PR to that issue and close it on merge.

## Sync Faculty Dropdown (`sync-faculty-dropdown.yml`)
- **Trigger Events:** Push modifying `_data/faculty-registry.csv`.
Reads the faculty registry CSV and automatically updates the selection dropdown options inside the issue template (`.github/ISSUE_TEMPLATE/faculty-profile.yml`).