FROM python:3.11-alpine

WORKDIR /app
COPY weather_service.py .
RUN pip install --no-cache-dir requests

CMD ["python", "weather_service.py"]
