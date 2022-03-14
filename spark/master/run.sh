sudo docker run -d -it --name spark-master --restart always --network=spark -e SPARK_MODE=master -e SPARK_MASTER_HOST=spark-master -p 7077:7077 -p 8080:8080 bitnami/spark:3.2.1
