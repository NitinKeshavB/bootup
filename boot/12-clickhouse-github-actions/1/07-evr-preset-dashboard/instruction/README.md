# Instruction 

Let's create a dashboard that visualises data from Clickhouse in near-real time. 

## Steps 

1. Create a database connection to clickhouse. Use the following parameters: 
    - SQL Alchemy URI: `clickhousedb://<username>:<password>@<hostname>:<port>/<database>` 
    - SQL Alchemy URI (example): `clickhousedb://default:mypassword@myhost.ap-southeast-1.aws.clickhouse.cloud:8443/default` 

    ![](images/clickhouse-connection.png)

    ![](images/clickhouse-connection2.png)

2. Create a dataset with the following metric: 
    ```yaml
    - metric_name: pull_request_count
    - label: pull_request_count
    - sql_expression: sum(case when event_type = 'PullRequestEvent' then 1 else 0 end)
    ```
3. Create a visual. 
    - Time column: `created_at` 
    - Metrics: `pull_request_count` 

    ![](images/line-chart.png)

4. Create a dashboard 
    - Set auto-refresh interval to `10 seconds`. 

    ![](images/auto-refresh.png)
    ![](images/dashboard.png)

5. Truncate data and insert data 
    - Truncate data in Clickhouse by running `truncate table github;` 
    - Run kafka producer again to insert all records with `num_messages=-1`: `python producer.py -f github.config -t github`
    - Watch the dashboard automatically update with new values in near-real time!  

