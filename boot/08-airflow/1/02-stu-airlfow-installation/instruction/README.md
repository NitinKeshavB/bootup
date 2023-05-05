# Instruction

## Task
Start Airflow standalone mode
1. Create a folder called `airflow`, this will be the place for your Airflow installation
2. Create a `dags` folder, copy the `dag_example` folder into it
3. `cd airflow`, start the airflow docker container `docker run -p 8080:8080 -v /$(pwd):/opt/airflow apache/airflow:2.4.0 standalone`
4. Log into the UI 
   - url: `localhost:8080`
   - username: `admin`
   - password: check standalone_admin_password.txt
5. Explore the UI
6. Enable the DAG called `example_bash_operator`
7. Manually trigger the DAG as well
8. `docker ps` to find the running container
9. `docker exec -it <container_id> bash` to get into it
10. `airflow --help` to checkout some commandlines

(Optional)
Install a new Python env
```
conda create -n airflow_env python=3.7.14
conda activate airflow_env
cd <your_project_dir>/08-airflow/1/01-ins-airflow-installation/unsolved # change directory to where the requirements.txt is stored
pip install -r requirements.txt
```