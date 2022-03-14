# sudo rm -rf /data/kafka$1/*
sudo docker run -d -it --name kafka$1 -p 30303:30303 --restart always --env-file $(pwd)/kafka$1/kafka$1.env -v /data/kafka$1/logs:/opt/kafka/logs -v /data/kafka$1/datalog:/kafka wurstmeister/kafka
