sudo docker run -it -d --restart always --name airflow-webserver -p 8080:8080 --env-file airflow-webserver.env apache/airflow:2.2.2 webserver
