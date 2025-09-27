from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ExampleJob").getOrCreate()

data = [("Bob", 1), ("James", 2)]
df = spark.createDataFrame(data, ["name", "id"])
df.show()

spark.stop()