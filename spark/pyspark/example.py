from pyspark.sql import SparkSession
spark = SparkSession.builder.master("spark://spark-master:7077").appName("TestApp").getOrCreate()
# do something
spark.stop()
