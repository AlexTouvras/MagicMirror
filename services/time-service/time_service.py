from datetime import datetime
import time

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[TIME SERVICE] {now}", flush=True)
    time.sleep(10)
