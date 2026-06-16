from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

spark = SparkSession.builder.appName("EcommerceETL").getOrCreate()

# -----------------------------
# READ RAW DATA
# -----------------------------
df = spark.read.option("header", True).csv("s3://project-ecommerce-pipeline/raw/orders/")

# -----------------------------
# CLEAN DATA
# -----------------------------
df = df.dropna()

# Convert numeric fields
df = df.withColumn("Amount", col("Amount").cast("double"))

# -----------------------------
# DATA QUALITY CHECKS
# -----------------------------

# Rule 1: No NULL Order ID
if df.filter(col("Order ID").isNull()).count() > 0:
    raise Exception("DQ Failed: NULL Order ID")

# Rule 2: No negative Amount
if df.filter(col("Amount") < 0).count() > 0:
    raise Exception("DQ Failed: Negative Amount")

print("✅ Data quality checks passed")

# -----------------------------
# DEDUPLICATION LOGIC
# -----------------------------

window_spec = Window.partitionBy("Order ID").orderBy(col("ingestion_time").desc())

df = df.withColumn("row_num", row_number().over(window_spec)) \
    .filter(col("row_num") == 1) \
    .drop("row_num")

print("✅ Deduplication done")

# -----------------------------
# WRITE PROCESSED DATA
# -----------------------------

df.write.mode("overwrite").parquet(
    "s3://project-ecommerce-pipeline/processed/orders/"
)

print("✅ Data written to processed layer")