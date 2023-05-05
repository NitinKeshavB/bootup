#!/bin/sh 

# create api image 
docker build . -t hello_world_api:1.0

# create hello_world image 
docker build . -t hello_world:1.0

# create network 
docker network create hello_world

# run api container 
docker run --rm -d -p 5000:5000 -e API_KEY=your_api_key -e CITY=your_city --network hello_world --name hello_world_api hello_world_api:1.0

# run hello_world container 
docker run --rm -e API_ENDPOINT=hello_world_api:5000 -e NAME=your_name --network hello_world --name hello_world hello_world:1.0
