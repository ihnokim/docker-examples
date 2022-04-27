sudo docker run -it --rm --name airflow-db-init --env-file airflow-db-init.env apache/airflow:2.2.2 airflow db init
