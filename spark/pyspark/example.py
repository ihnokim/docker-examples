import socket
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


def get_pod_domain_name():
    ip_addr = socket.gethostbyname(socket.gethostname())
    return '%s.spark.pod.cluster.local' % ip_addr.replace('.', '-')


spark_conf = SparkConf()
spark_conf.setAll([
    ('spark.master', 'spark://10.0.2.3:30077'),
    ('spark.app.name', 'TestApp'),
    ('spark.submit.deployMode', 'client'),
    ('spark.ui.showConsoleProgress', 'true'),
    ('spark.eventLog.enabled', 'false'),
    ('spark.logConf', 'false'),
    ('spark.driver.bindAddress', '0.0.0.0'),
    ('spark.driver.host', get_pod_domain_name()),
])


# spark = SparkSession.builder.master("spark://spark-master:7077").appName("TestApp").getOrCreate()
spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize(range(10000))
ret = rdd.sum()
spark.stop()
