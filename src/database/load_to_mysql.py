import mysql.connector
import pandas as pd

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="job_data_platform"
)

print("MySQL connection successful!")

# Read the processed Parquet data
df = pd.read_parquet(
    "data/processed/parquet/jobs"
)

# Convert pandas NaN values to Python None
# so MySQL stores them as NULL
# Replace all NaN values with None
df = df.astype(object).where(pd.notna(df), None)
print("Jobs loaded from Parquet:", len(df))

# Create cursor
cursor = connection.cursor()

# Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS jobs (
    job_id VARCHAR(64) PRIMARY KEY,
    title TEXT,
    company VARCHAR(255),
    location VARCHAR(255),
    salary_min DOUBLE,
    salary_max DOUBLE,
    salary_period VARCHAR(50),
    currency VARCHAR(20),
    experience TEXT,
    skills TEXT,
    employment_type VARCHAR(100),
    posted_date BIGINT,
    expiry_date BIGINT,
    application_url TEXT,
    source VARCHAR(100)
)
"""

cursor.execute(create_table_query)

cursor.execute("TRUNCATE TABLE jobs")

# Insert data
insert_query = """
INSERT INTO jobs (
    job_id,
    title,
    company,
    location,
    salary_min,
    salary_max,
    salary_period,
    currency,
    experience,
    skills,
    employment_type,
    posted_date,
    expiry_date,
    application_url,
    source
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():

    cursor.execute(
        insert_query,
        (
            row["job_id"],
            row["title"],
            row["company"],
            row["location"],
            row["salary_min"],
            row["salary_max"],
            row["salary_period"],
            row["currency"],
            str(row["experience"]),
            str(row["skills"]),
            row["employment_type"],
            row["posted_date"],
            row["expiry_date"],
            row["application_url"],
            row["source"]
        )
    )

connection.commit()

print("Data successfully loaded into MySQL!")

# Verify
cursor.execute("SELECT COUNT(*) FROM jobs")

count = cursor.fetchone()[0]

print("Total jobs in MySQL:", count)

cursor.close()
connection.close()