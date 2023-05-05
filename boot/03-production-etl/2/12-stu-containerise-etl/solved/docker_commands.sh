#!/bin/sh 

# build docker container 
docker build . -t <your_name>/dvd_store_etl:1.0

# run docker container 
docker run --rm --env-file .env <your_name>/dvd_store_etl:1.0
