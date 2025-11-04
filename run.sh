#!/usr/bin/env bash
# Simple helper to run the game from the workspace root.
set -euo pipefail

PY=python
VENV_DIR="venv"

if [ -d "$VENV_DIR" ] && [ -f "$VENV_DIR/bin/activate" ]; then
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
fi

exec "$PY" "card game/main.py"
