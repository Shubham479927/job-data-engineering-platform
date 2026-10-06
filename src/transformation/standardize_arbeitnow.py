import json
import hashlib
import os

RAW_FILE = "data/raw/arbeitnow_jobs.json"


def standardize_job(job):

    job_string = (
        f"{job.get('company_name')}|"
        f"{job.get('title')}|"
        f"{job.get('url')}"
    )

    job_id = hashlib.sha256(
        job_string.encode("utf-8")
    ).hexdigest()

    standardized_job = {
        "job_id": job_id,
        "title": job.get("title"),
        "company": job.get("company_name"),
        "location": job.get("location"),
        "salary_min": None,
        "salary_max": None,
        "salary_period": None,
        "currency": None,
        "experience": None,
        "skills": job.get("tags"),
        "employment_type": job.get("job_types"),
        "posted_date": job.get("created_at"),
        "expiry_date": None,
        "application_url": job.get("url"),
        "source": "arbeitnow"
    }

    return standardized_job


with open(RAW_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

jobs = data["data"]

standardized_jobs = []

for job in jobs:
    standardized_jobs.append(
        standardize_job(job)
    )

print("Total standardized jobs:", len(standardized_jobs))

os.makedirs("data/processed", exist_ok=True)

OUTPUT_FILE = "data/processed/arbeitnow_jobs_standardized.json"

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(
        standardized_jobs,
        file,
        indent=4,
        ensure_ascii=False
    )

print("Standardized Arbeitnow data saved successfully.")