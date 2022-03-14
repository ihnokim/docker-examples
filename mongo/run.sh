# sudo mkdir /data
# sudo mkdir /data/mongo$1
sudo docker run --name mongo$1 --restart always --env-file mongo$1/mongo$1.env -v /data/mongo$1/db:/data/db -d -p 27017:27017 mongo:3.6
