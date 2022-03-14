sudo docker run -d -it --name spark-worker$1 --network=spark -e SPARK_MODE=worker -e SPARK_MASTER_URL=spark://spark-master:7077 -e SPARK_WORKER_WEBUI_PORT=808$1 -p 808$1:808$1 bitnami/spark:3.2.1
