# Instruction

## Task

1. Put the dbt project folder in the `dbt` folder under `dags`
    ```
    |-- dag_etl
    |-- dag_example
    |-- dag_practice
    |-- dbt
    |-- function
    ```
2. Store env vars in json format in Airflow Variables `DBT_ENV`. It can be referred by `"{{ var.json.DBT_ENV }}"`.
3. The way we installed dbt, it is installed at `/usr/local/airflow/dbt_env/bin/dbt` in a virtual environment called `dbt_env`.
4. In the bash code, what we do is
   1. Copy dbt project code to `/tmp`
   2. CD into the dbt project
   3. run `dbt deps`
   4. run `dbt build`
   5. print run logs  

    ```
    cp -R /opt/airflow/dags/dbt /tmp;\
    cd /tmp/dbt/decdotcom;\
    /usr/local/airflow/dbt_env/bin/dbt deps;\
    /usr/local/airflow/dbt_env/bin/dbt build --project-dir /tmp/dbt/decdotcom/ --profiles-dir . --target prod;\
    cat /tmp/dbt_logs/dbt.log"
    ```
