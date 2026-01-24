#!/usr/bin/env bash
set -euo pipefall
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ "{1:-}" = "" ]; then
   docker compose logs -f --tail=200
else
   docker compose logs -f --tail=200 "$1"
fi
