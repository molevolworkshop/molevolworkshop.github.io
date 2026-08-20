#!/bin/bash

REPO_URL="https://github.com/molevolworkshop/moledata"
DEST_DIR="materials"

if [ -d "$DEST_DIR/.git" ]; then
    echo "Existing repository found in '$DEST_DIR'. Pulling latest updates..."
    git -C "$DEST_DIR" pull
else
    echo "Cloning '$REPO_URL' into '$DEST_DIR'..."
    git clone --depth 1 "$REPO_URL" "$DEST_DIR"
fi

git -C materials lfs pull



bundle exec jekyll serve