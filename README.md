\# Multi-Source Job Data Engineering \& Analytics Platform



An end-to-end data engineering and analytics project that collects job listings from multiple public job APIs, standardizes and validates the data, processes it using Apache Spark, stores the processed data in MySQL, and visualizes job-market insights using Power BI.



\## Project Overview



Job data from different sources often has inconsistent schemas, formats, employment types, experience levels, locations, and missing values.



This project builds a complete data pipeline to transform raw job listings into a structured dataset that can be used for analytics and business intelligence.



\## Data Pipeline



Job APIs

↓

Raw JSON Data

↓

Data Standardization

↓

Data Validation

↓

PySpark Processing

↓

Parquet Dataset

↓

MySQL Database

↓

Power BI Dashboard



\## Data Sources



\### Himalayas



\- Jobs collected through the Himalayas public API

\- Records collected: 20



\### Arbeitnow



\- Jobs collected through the Arbeitnow public API

\- Records collected: 326



\### Combined Dataset



Total processed jobs: \*\*346\*\*



| Source | Jobs |

|---|---:|

| Himalayas | 20 |

| Arbeitnow | 326 |

| \*\*Total\*\* | \*\*346\*\* |



\## Technologies Used



\- Python

\- REST APIs

\- Requests

\- Pandas

\- NumPy

\- Apache PySpark

\- PyArrow / Parquet

\- MySQL

\- Power BI

\- Git / GitHub



\## Project Structure



```text

job-data-engineering-platform/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── src/

│   ├── ingestion/

│   │   ├── arbeitnow\_api.py

│   │   └── job\_api.py

│   │

│   ├── transformation/

│   │   ├── combine\_jobs.py

│   │   ├── standardize.py

│   │   └── standardize\_arbeitnow.py

│   │

│   ├── validation/

│   │   ├── validator.py

│   │   └── combined\_validator.py

│   │

│   ├── processing/

│   │   └── spark\_jobs.py

│   │

│   └── database/

│       └── load\_to\_mysql.py

│

├── tests/

├── logs/

├── .gitignore

├── requirements.txt

└── README.md

