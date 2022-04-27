from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.setAll([
        ('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem'),
        ('spark.hadoop.fs.s3a.access.key', '***'),
        ('spark.hadoop.fs.s3a.secret.key', '***'),
        ('spark.hadoop.fs.s3a.endpoint', 'http://x.x.x.x:xxxx'),
        ('spark.hadoop.fs.s3a.path.style.access', 'true'),
        ('spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version', '2'),
        # ('spark.hadoop.mapreduce.fileoutputcommitter.cleanup-failures.ignored', 'true'),
        # ('spark.hadoop.mapreduce.fileoutputcommitter.cleanup.skipped', 'true'),
        ('spark.hadoop.fs.s3a.multiobjectdelete.enable', 'false'),
        ('spark.hadoop.fs.s3a.chnage.detection.version.required', 'false'),
        ('spark.hadoop.fs.s3a.change.detection.mode', 'none')
    ])
    spark = SparkSession.builder.config(conf=spark_conf).appName('S3JoinExample').getOrCreate()

    data_dir = 's3a://bucket/spark/data/'
    filenames = [data_dir + 'test%s.csv' % i for i in range(1, 4)]
    dfs = dict()
    for filename in filenames:
        dfs[filename] = spark.read.csv(filename, header=True)
    result = None
    for df in dfs.values():
        if result is None:
            result = df
        else:
            result = result.join(df, on=['column1', 'column2', 'column3'], how='outer')
    result.write.csv('file:///opt/spark/local-fs/spark/results/csv_join_example', header=True)
    spark.stop()
