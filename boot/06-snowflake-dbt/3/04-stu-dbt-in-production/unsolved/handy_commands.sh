dbt clean

cd ..

docker build -t dbtbuild -f docker/Dockerfile .

# For windows users, try docker command first, it should work. If is asked, add `winpty` before docker for tty
# For mac users, you should be able to run docker command directly
docker run -it --entrypoint bash dbtbuild
# Once in, run `ls` to check if files are copied as expected, run `exit` to exit

# This command is to check if your docker image run as expected
# Note that your env file path might be different
docker run --env-file docker/dbt.env dbtbuild

docker tag dbtbuild:latest <many_digits_here>.dkr.ecr.ap-southeast-2.amazonaws.com/dbtbuild:latest

docker images

aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin <many_digits_here>.dkr.ecr.ap-southeast-2.amazonaws.com/dbtbuild

docker push <many_digits_here>.dkr.ecr.ap-southeast-2.amazonaws.com/dbtbuild:latest