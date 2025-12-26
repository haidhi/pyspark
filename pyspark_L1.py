from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("VSCodeTest").getOrCreate()
df = spark.createDataFrame([(1, "Ali"), (2, "Sara")], ["id", "name"])
df.show()
spark.stop()
