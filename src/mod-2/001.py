from pyspark.sql import SparkSession


spark = (
    SparkSession
    .builder
    .getOrCreate()
)

sc = spark.sparkContext

print("SparkContext initialized successfully.")
print(f"Spark Version: {spark.version}")
print(f"Application ID: {sc.ApplicationId}")
print(f"Available Cores: {sc.DefaultParallelism}")


spark.stop()