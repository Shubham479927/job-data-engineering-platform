import json
import os
import hashlib

RAW_FILE ="data/raw/himalayas_jobs.json"

def standardize_job(job):
    job_string = (
        f"{job.get('companyName')}|"
        f"{job.get('title')}|"
        f"{job.get('applicationLink')}"
    )

    job_id = hashlib.sha256(
        job_string.encode("utf-8")
    ).hexdigest()
        
    standardized_job ={
        "job_id" : job_id,
        "title" : job.get("title"),
        "company" : job.get("companyName"),
        "location": job.get("locationRestrictions"),
        "salary_min": job.get("minSalary"),
        "salary_max": job.get("maxSalary"),
        "salary_period": job.get("salaryPeriod"),
        "currency": job.get("currency"),
        "experience": job.get("seniority"),
        "skills": job.get("categories"),
        "employment_type": job.get("employmentType"),
        "posted_date": job.get("pubDate"),
        "expiry_date": job.get("expiryDate"),
        "application_url": job.get("applicationLink"),
        "source": "himalayas"        
    }
    
    return standardized_job

with open(RAW_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)
    
jobs = data["jobs"]

standardized_jobs = []

for job in jobs:
    standardized_jobs.append(standardize_job(job))

print("Total standardized jobs:", len(standardized_jobs))

# print("Standardized job:")
# print(standardize_job)
os.makedirs("data/processed", exist_ok=True)

OUTPUT_FILE = "data/processed/himalayas_jobs_standardized.json"

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(standardized_jobs, file, indent=4, ensure_ascii=False)

print("Standardized data saved successfully.")