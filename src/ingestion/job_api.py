import requests
import json
import os

API_url ="https://himalayas.app/jobs/api"

response = requests.get(
    API_url,
    params={"limit":20}
    )

print("Status code:",response.status_code)

data = response.json()

# print("\nAvailable fields in a job:")
# print(data["jobs"][0].keys())

print("Total jobs:",data["totalCount"])
print("Jobs recived:",len(data["jobs"]))

# Create raw data directory if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# save raw api responce
with open("data/raw/himalayas_jobs.json","w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
    
print("Raw data saved successfully.")
    
