#!/bin/bash
set -e

REPO_URL="https://github.com/molevolworkshop/moledata"
DEST_DIR="materials"

echo "=== 1. Checking out / updating moledata materials ==="
if [ -d "$DEST_DIR/.git" ]; then
    echo "Existing repository found in '$DEST_DIR'. Pulling latest updates..."
    git -C "$DEST_DIR" pull
else
    echo "Cloning '$REPO_URL' into '$DEST_DIR'..."
    git clone --depth 1 "$REPO_URL" "$DEST_DIR"
fi

echo "=== 2. Pulling LFS assets ==="
git -C "$DEST_DIR" lfs install --local
git -C "$DEST_DIR" lfs pull

echo "=== 3. Scanning and generating index.md wrapper files ==="
find "$DEST_DIR/labs" -name "README.md" | while read -r readme_file; do
    dir_path=$(dirname "$readme_file")
    index_file="$dir_path/index.md"
    
    # Copy README.md to index.md so Jekyll builds it at the clean directory URL
    cp "$readme_file" "$index_file"
done

echo "=== Materials preparation complete! ==="