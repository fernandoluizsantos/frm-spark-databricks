from pyspark.sql import SparkSession


spark = (
    SparkSession
    .builder
    .getOrCreate()
)

sc = spark.sparkContext

print("SparkContext initialized successfully.")
print(f"Spark Version: {spark.version}")
print(f"Application ID: {sc.applicationId}")
print(f"Available Cores: {sc.defaultParallelism}")


spark.stop()