import datetime

import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from function.function import log_to_info, log_to_debug, log_to_warning

with DAG(
        dag_id='my_first_dag_stu',
        schedule_interval='0 6 * * *',
        start_date=pendulum.yesterday(tz="UTC"),
        catchup=False,
        dagrun_timeout=datetime.timedelta(minutes=5),
        tags=['MyFirst!'],
) as dag:
    data_interval_start = " {{ data_interval_start }} "

    info = PythonOperator(
        task_id='log_info',
        python_callable=log_to_info,
        op_kwargs={
            "txt": data_interval_start,
        }
    )

    debug = PythonOperator(
        task_id='log_debug',
        python_callable=log_to_debug,
        op_kwargs={
            "txt": data_interval_start,
        }
    )

    warning = PythonOperator(
        task_id='log_warning',
        python_callable=log_to_warning,
        op_kwargs={
            "txt": data_interval_start,
        }
    )

    warning >> info >> debug
