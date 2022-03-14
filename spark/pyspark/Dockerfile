FROM python:3.8-slim
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y vim openjdk-11-jre
RUN python -m pip install pip
RUN python -m pip install pyspark
WORKDIR /usr/src
