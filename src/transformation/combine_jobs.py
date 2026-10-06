import json
import os

HIMALAYAS_FILE = "data/processed/himalayas_jobs_standardized.json"
ARBEITNOW_FILE = "data/processed/arbeitnow_jobs_standardized.json"

with open(HIMALAYAS_FILE, "r", encoding="utf-8") as file:
    himalayas_jobs = json.load(file)

with open(ARBEITNOW_FILE, "r", encoding="utf-8") as file:
    arbeitnow_jobs = json.load(file)

all_jobs = himalayas_jobs + arbeitnow_jobs

print("Himalayas jobs:", len(himalayas_jobs))
print("Arbeitnow jobs:", len(arbeitnow_jobs))
print("Total jobs:", len(all_jobs))

os.makedirs("data/processed", exist_ok=True)

OUTPUT_FILE = "data/processed/all_jobs.json"

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(
        all_jobs,
        file,
        indent=4,
        ensure_ascii=False
    )

print("Combined jobs saved successfully.")