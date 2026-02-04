from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
import os

app = FastAPI(title="time-service")

def get_tz():
    name = os.getenv("TZ", "UTC")
    try:
        return ZoneInfo(name)
    except Exception:
        return ZoneInfo("UTC")

def part_of_day(hour: int) -> str:
    if 5 <= hour < 12:
        return "morning"
    if 12 <= hour < 17:
        return "afternoon"
    if 17 <= hour < 22:
        return "evening"
    return "night"

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "time-service",
        "version": os.getenv("SERVICE_VERSION", "dev"),
    }

@app.get("/time")
def time_now():
    now = datetime.now(get_tz())
    return {
        "iso": now.isoformat(),
        "timezone": os.getenv("TZ", "UTC"),
    }

@app.get("/context")
def context():
    now = datetime.now(get_tz())
    dow = now.strftime("%A")
    return {
        "day_of_week": dow,
        "is_weekend": dow in ("Saturday", "Sunday"),
        "part_of_day": part_of_day(now.hour),
        "local_hour": now.hour,
        "timezone": os.getenv("TZ", "UTC"),
    }
