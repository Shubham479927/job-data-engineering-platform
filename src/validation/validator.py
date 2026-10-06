import json

PROCESSED_FILE = "data/processed/himalayas_jobs_standardized.json"

with open(PROCESSED_FILE, "r", encoding="utf-8") as file:
    jobs = json.load(file)

print("Jobs loaded:", len(jobs))


required_fields = [
    "job_id",
    "title",
    "company"
]

for field in required_fields:
    missing_count = 0

    for job in jobs:
        if job.get(field) is None or job.get(field) == "":
            missing_count += 1

    print(f"{field}: {missing_count} missing")

job_ids = []

for job in jobs:
    job_ids.append(job.get("job_id"))

unique_job_ids = set(job_ids)

duplicate_count = len(job_ids) - len(unique_job_ids)

print("Duplicate job IDs:", duplicate_count)

invalid_salary_count = 0

for job in jobs:
    salary_min = job.get("salary_min")
    salary_max = job.get("salary_max")

    if salary_min is not None and salary_max is not None:
        if salary_min > salary_max:
            invalid_salary_count += 1

print("Invalid salary ranges:", invalid_salary_count)

invalid_date_count = 0

for job in jobs:
    posted_date = job.get("posted_date")
    expiry_date = job.get("expiry_date")

    if posted_date is not None and expiry_date is not None:
        if posted_date > expiry_date:
            invalid_date_count += 1

print("Invalid date ranges:", invalid_date_count)


