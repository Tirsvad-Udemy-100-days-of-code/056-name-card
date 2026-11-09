#!/usr/bin/env bash
# Take the lecture-step screenshots in a Docker container with a headless
# browser, so no GUI is driven on the host desktop (framework/process/gui-testing.md).
# Usage: bash tools/screenshots/run.sh      (from the repository root)
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
mkdir -p "$root/docs/screenshots"
MSYS_NO_PATHCONV=1 docker run --rm \
  -v "$root:/repo:ro" -v "$root/docs/screenshots:/out" \
  mcr.microsoft.com/playwright/python:v1.54.0-noble \
  bash -c "pip install --quiet --break-system-packages flask playwright==1.54.0 && python /repo/tools/screenshots/capture.py"
