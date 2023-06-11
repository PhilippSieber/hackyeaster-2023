TAG=he2023/ring2
NAME=he2023-ring2

sudo docker build -t $TAG .
sudo docker stop $NAME
id=$(sudo docker run --rm -p 1337:45678 -d --name $NAME -t $TAG)
sudo docker cp $id:/challenge/main ./src/main
