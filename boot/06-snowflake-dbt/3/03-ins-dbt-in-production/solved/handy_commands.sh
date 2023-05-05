dbt clean

cd ..

docker build -t dbtbuild -f docker/Dockerfile .

docker run -it --entrypoint bash dbtbuild

docker run --env-file docker/dbt.env dbtbuild

docker tag dbtbuild:latest 931718146526.dkr.ecr.ap-southeast-2.amazonaws.com/dbtbuild:latest

docker images

aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 931718146526.dkr.ecr.ap-southeast-2.amazonaws.com/dbtbuild

docker push 931718146526.dkr.ecr.ap-southeast-2.amazonaws.com/dbtbuild:latest