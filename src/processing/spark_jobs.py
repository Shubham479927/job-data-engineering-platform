import os

os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"
os.environ["PATH"] = r"C:\hadoop\bin;" + os.environ["PATH"]

from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

spark = (
    SparkSession.builder
    .appName("JobDataProcessing")
    .master("local[*]")
    .config(
        "spark.hadoop.fs.file.impl",
        "org.apache.hadoop.fs.RawLocalFileSystem"
    )
    .getOrCreate()
)

INPUT_FILE = "data/processed/all_jobs.json"

df = (
    spark.read
    .option("multiLine", True)
    .json(INPUT_FILE)
)

df = (
    df.withColumn(
        "location",
        regexp_replace(col("location"), r'[\[\]"\r\n]', "")
    )
    .withColumn(
        "location",
        regexp_replace(col("location"), r'\s+', " ")
    )
    .withColumn(
        "location",
        regexp_replace(col("location"), r'^\s+|\s+$', "")
    )
)

print("Total jobs:", df.count())

print("\nSchema:")
df.printSchema()

print("\nSample data:")
df.show(5, truncate=False)

print("\nLocation examples:")
df.select("source", "location").show(20, truncate=False)

OUTPUT_PATH = "data/processed/parquet/jobs"

df.write \
    .mode("overwrite") \
    .parquet(OUTPUT_PATH)

print("\nParquet data saved successfully.")

spark.stop()