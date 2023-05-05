### Instruction

## Task
Write a DAG and a task to extract data from Alpaca.
Create `alpaca_etl1.py` and `alpaca_functions.py` as below.

```
dags
|-- dag_example
|-- dag_practice
|-- dag_etl
  |-- alpaca_etl1.py
|-- function
  |-- function.py (from previous exercise)
  |-- alpaca_functions.py
```

Checklist:
1. Alpaca API Connection created in Airflow (Host: https://data.alpaca.markets, headers in JSON format in Extra)
2. AWS Connection created in Airflow
3. S3 bucket created and its name stored in Variable
4. Use hardcoded `symbol = "AAPL"` for now in your DAG file
5. the `extract` function takes the below parameters:
   1. s3_conn_id
   2. s3_bucket
   3. api_conn_id
   4. symbol
   5. data_interval_start
   6. data_interval_end

Some helpers:
1. `endpoint=f"/v2/stocks/{symbol}/trades?"`
2. `resp.json().get("trades")`
3. `s3://{s3_bucket}/landing/{data_interval_end}/{symbol}_{data_interval_end}.json`
4. `json.dump()`
5. `http_hook.run()`
6. `s3_hook.load_file()`