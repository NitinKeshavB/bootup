#!/bin/sh 

# build docker container 
docker build . -t <your_name>/dellstore_etl:1.0

# run docker container 
docker run --rm --env-file .env <your_name>/dellstore_etl:1.0
