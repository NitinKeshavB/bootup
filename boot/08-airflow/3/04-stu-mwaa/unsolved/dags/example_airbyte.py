import datetime
import pendulum

from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteHook
from airflow.operators.python import PythonOperator

with DAG(
        dag_id='example_airbyte',
        schedule_interval='0 0 * * *',
        start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
        catchup=False,
        render_template_as_native_obj=True,
        dagrun_timeout=datetime.timedelta(minutes=5),
        tags=['example'],
) as dag:

    def func(airbyte_conn_id):
        airbyte_hook = AirbyteHook(airbyte_conn_id)
        print(airbyte_hook.test_connection())

    airbyte_conn_id = 'airbyte_decsydliu'
    test_airbyte = PythonOperator(
        task_id="test_airbyte",
        python_callable=func,
        op_kwargs={
            "airbyte_conn_id": airbyte_conn_id,
        }
    )
