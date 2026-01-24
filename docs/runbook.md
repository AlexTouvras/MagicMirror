# Smart Mirror Backed - Runbook

## What this is 
Containerized backed services running on a Raspberry Pi using Docker Compose.
Autostart is handled by systemd.

Repo location on Pi:
- /home/pi/smart-mirror-backend

## Services & Ports
- time-service:http://localhost:8010
-weather-service: http://localhost:8020

Health endpoints:
- GET /health

Time-service endpoints:
- GET /time
- GET /context

## Start/Stop (systemd)
Start:
- sudo systemctl start smart-mirror.backend.service

Stop:
- sudo systemctl stop smart-mirror-backend.service

Status:
- sudo systemctl status smart-mirror-backend.service --no-pager
- sudo journalctl -u smart-mirror-backend.service -b --no-pager -n 200

## Start/Stop )manual via Compose)
From /home/pi/smart-mirror-backend:
- docker compose up -d
- docker compose down 
- docker compose ps
- docker compose logs -f time-service

## Config (.env)
- .env is local-only (ignored by git)
- .env.example is the template

After changing .env:
Run on PI: 
- python3 -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8010/health').read().decode())"
- python3 -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8020/health').read().decode())"

## Deployment (safe + deterministic)
Boot should NOT build images

Recommended deploy flow:
1) git pull
2) docker compose build 
3) docker compose up -d --remove-orphans 
4) verify /health endpoints 
