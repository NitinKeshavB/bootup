# create a new virtual environment so that our python env get the same core packages as the docker image
conda create -n airflow_env python=3.7.14
conda activate airflow_env
cd <your_project_dir>/08-airflow/1/01-ins-airflow-installation/unsolved # change directory to where the requirements.txt is stored
pip install -r requirements.txt

# start container, safe to close the command window once the image is up
# you can use the full path rather than $(pwd)
docker run -p 8080:8080 -v /$(pwd):/opt/airflow apache/airflow:2.4.0 standalone

# check id of running container:
docker ps

# bash into a running container:
docker exec -it <yout_container_id> bash

# access ui at
http://localhost:8080

# user:
admin

# password:
stored in standalone_admin_password.txt