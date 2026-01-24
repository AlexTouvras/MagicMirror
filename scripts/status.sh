#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
echo "== systemd =="
sudo systemctl status smart-mirror-backend.service --no-pager || true
echo
echo "== compose =="
docker compose ps
