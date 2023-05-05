import datetime
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from function.etl import extract

with DAG(
        dag_id='weather_etl1',
        schedule_interval='0 0 * * *',
        start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
        catchup=False,
        dagrun_timeout=datetime.timedelta(minutes=5),
        tags=['weather'],
) as dag:
    data_interval_end = "{{ data_interval_end.format('YYYYMMDDHHmmss') }}"

    aws_conn_id = "aws_decsydliu"
    s3_bucket = "{{ var.value.S3_BUCKET }}"
    s3_key_ref_cities = "{{ var.value.S3_KEY_REF_CITIES }}"

    api_conn_id = "weather_api"
    weather_api_key = "{{ var.value.WEATHER_API_KEY }}"

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
        op_kwargs={
            "s3_conn_id": aws_conn_id,
            "s3_bucket": s3_bucket,
            "s3_key_ref_cities": s3_key_ref_cities,
            "api_conn_id": api_conn_id,
            "api_key": weather_api_key,
            "data_interval_end": data_interval_end
        }
    )
