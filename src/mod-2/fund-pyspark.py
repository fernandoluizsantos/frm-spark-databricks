from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, lit, current_timestamp


spark = (
    SparkSession
        .builder
        .getOrCreate()
)

sc = spark.sparkContext

# (1) INGESTION OF RESTAURANTS DATA
restaurants_path_json = "/opt/bitnami/spark/storage/mysql/restaurants/*.jsonl"
restaurants_schema = StructType([
    StructField("country", StringType(), True),
    StructField("city", StringType(), True),
    StructField("restaurant_id", LongType(), True),
    StructField("phone_number", StringType(), True),
    StructField("cnpj", StringType(), True),
    StructField("average_rating", DoubleType(), True),
    StructField("name", StringType(), True),
    StructField("uuid", StringType(), True),
    StructField("address", StringType(), True),
    StructField("opening_time", StringType(), True),
    StructField("cuisine_type", StringType(), True),
    StructField("closing_time", StringType(), True),
    StructField("num_reviews", LongType(), True),
    StructField("dt_current_timestamp", TimestampType(), True),
])

df_restaurants = (
    spark
    .read
    .schema(restaurants_schema)
    .option("multiline", "true")
    .option("mode", "PERMISSIVE")
    .json(restaurants_path_json)
)
df_restaurants.printSchema()


# (2) TRANSFORMATION OF RESTAURANTS DATA
df_restaurants_col_select = df_restaurants.select(
    col("cuisine_type"),
    col("num_reviews"),
    col("opening_time"),
    col("closing_time"),
)

df_restaurants_col_select.show(5, truncate=False)


spark.stop()