def extract(s3_conn_id, s3_bucket, api_conn_id, symbol, data_interval_start, data_interval_end):
    import json
    import os
    from airflow.providers.http.hooks.http import HttpHook
    from airflow.providers.amazon.aws.hooks.s3 import S3Hook

    s3_hook = S3Hook(aws_conn_id=s3_conn_id)
    http_hook = HttpHook(method="GET", http_conn_id=api_conn_id)
    expected_new_key = f's3://{s3_bucket}/landing/{data_interval_end}/{symbol}_{data_interval_end}.json'

    params = {
        "start": data_interval_start,
        "end": data_interval_end
    }

    # call api
    resp = http_hook.run(endpoint=f"/v2/stocks/{symbol}/trades?", data=params)

    # serialise the json file into landing/
    if resp.status_code == 200:
        alpaca_data = resp.json().get("trades")
        filename = expected_new_key.split("/")[-1]
        tmp_file = f"/tmp/{filename}"
        with open(tmp_file, 'w') as f:
            json.dump(alpaca_data, f)
        s3_hook.load_file(filename=tmp_file, key=expected_new_key, replace=True)
        os.unlink(tmp_file)

    return expected_new_key

def transform(s3_conn_id, s3_bucket, s3_keys, s3_key_ref_exchange_codes, data_interval_end):
    import pandas as pd
    import json
    from airflow.providers.amazon.aws.hooks.s3 import S3Hook
    import os

    # get json file, read into df
    # <YOUR CODE HERE>

    df_quotes_renamed = df.rename(columns={
        "t": "timestamp",
        "x": "exchange",
        "p": "price",
        "s": "size",
    })

    df_quotes_selected = df_quotes_renamed[['timestamp', 'exchange', 'price', 'size']]

    # get exchange codes file, read into df_exchange_codes
    # <YOUR CODE HERE>

    df_exchange = pd.merge(left=df_quotes_selected, right=df_exchange_codes,
                           left_on="exchange", right_on="exchange_code") \
        .drop(columns=["exchange_code", "exchange"]) \
        .rename(columns={"exchange_name": "exchange"})

    # remove duplicates by doing a group by on the keys: timestamp and exchange
    # get the mean of price, and sum of size
    df_ask_bid_exchange_de_dup = df_exchange.groupby(["timestamp", "exchange"]).agg({
        "price": "mean",
        "size": "sum",
    }).reset_index()

    # uploading back to s3 in the staging layer
    # <YOUR CODE HERE>

    return expected_new_key
