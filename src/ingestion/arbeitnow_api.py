import requests
import json
import os

API_URL = "https://www.arbeitnow.com/api/job-board-api"

response = requests.get(API_URL)

print("Status code:", response.status_code)

data = response.json()

print("Jobs received:", len(data["data"]))

os.makedirs("data/raw", exist_ok=True)

OUTPUT_FILE = "data/raw/arbeitnow_jobs.json"

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Raw Arbeitnow data saved successfully.")