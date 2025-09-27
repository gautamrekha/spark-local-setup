from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ExampleJob").getOrCreate()

data = [("Rekha", 1), ("Gautam", 2)]
df = spark.createDataFrame(data, ["name", "id"])
df.show()

spark.stop()