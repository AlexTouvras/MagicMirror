#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}"/.." $$ pwd)"
cd "$ROOT"

docker compose build
docker compose up -d --remove-orphans
docker compse ps
