# sudo rm -rf /data/zoo$1/*
sudo docker run -d -it --name zoo$1 -p 21810:2181 -p 2888:2888 -p 3888:3888 -p 4888:8080 -v /data/zoo$1/logs:/logs -v /data/zoo$1/datalog:/datalog -v /data/zoo$1/data:/data --restart always --env-file $(pwd)/zoo$1/zoo$1.env ihnokim/zookeeper
