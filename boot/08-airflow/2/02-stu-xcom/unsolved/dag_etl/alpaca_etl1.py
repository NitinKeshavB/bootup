import datetime
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from function.alpaca_functions import extract

with DAG(
        dag_id='alpaca_etl1',
        schedule_interval='0 0 * * *',
        start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
        catchup=False,
        dagrun_timeout=datetime.timedelta(minutes=5),
        tags=['weather'],
) as dag:
    data_interval_start = "{{ data_interval_start.to_rfc3339_string() }}"
    data_interval_end = "{{ data_interval_end.to_rfc3339_string() }}"

    aws_conn_id = "aws_decsydliu"
    s3_bucket = "{{ var.value.S3_BUCKET_ALPACA }}"

    api_conn_id = "alpaca_api"

    symbol = "AAPL"

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
        op_kwargs={
            "s3_conn_id": aws_conn_id,
            "s3_bucket": s3_bucket,
            "api_conn_id": api_conn_id,
            "symbol": symbol,
            "data_interval_start": data_interval_start,
            "data_interval_end": data_interval_end
        }
    )
