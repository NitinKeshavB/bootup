# Capstone Project

## Context 

You have made it to the end of the bootcamp! :clap:

Over the past 12 weeks, you have learnt: 
- How to build data integration pipelines (extract load) using data integration tools like Airbyte
- How to use big data compute engines to transform data i.e. Snowflake and Databricks (Spark) 
- How to create data transformation pipelines using tools like dbt 
- How to orchestrate data integration and data transformation pipelines using a data orchestration tool like Airflow
- How to ingest and transform real-time data using Kafka, kSQLdb, and Clickhouse 
- How to perform data modelling using techniques such as Kimball's Dimensional Model
- How to perform semantic data modelling and data visualization (batch or near real-time) using tools like Preset (Superset)
- How to use git to commit code and collaborate with teams using branches 
- How to create CI/CD pipelines to automate code testing, integration, and deployment 
- How to package and host the various components on Amazon Web Services (AWS) or SaaS cloud offerings (e.g. Airbyte Cloud, Clickhouse Cloud, Confluent Cloud, Databricks Cloud, Snowflake Cloud, etc)


## Goal

- Work as an **individual** or in a **team** to create either a batch and/or real-time ETL solution. 
- Your ETL solution should serve the goal of serving a use-case such as: 
    - An analytical dashboard with data refreshes in batches or near-real time 
    - Generating predictions using machine learning model 
- Your data pipeline must have the potential to scale horizontally to handle terrabytes or petabytes of data. This can be achieved by adding more nodes to a Spark or Snowflake cluster, or adding more brokers to a Kafka cluster, or adding more shards to a Clickhouse cluster. However, for practical reasons, you are not required to use terrabyte or petabyte size datasets for this project. 
- You may choose any dataset(s) or data producer(s) that you and your team would like to work with. For example, you may choose a REST API endpoint with data updating every few minutes, or an application database with Change Data Capture (CDC) enabled, or a kafka producer mimicking a IoT sensor. 
- Model your data using data modelling techniques like dimensional modelling and 3NF 
- Your ETL pipeline should have data quality tests where possible. 
- Deploy and schedule your ETL pipeline on the cloud where possible. 
- Create continuous integration and deployment pipelines to automate the integration and deployment of your application. 
- Present and demo your working solution to the class. 

Here are some data sources (this is not an extensive list and you are encouraged to do your own research): 

|Data source name|Data source type|URL|
|--|--|--|
|Public APIs| REST API | https://github.com/public-apis/public-apis| 
|Australian Government Open Source Datasets|  REST API, CSV | https://data.gov.au/| 
|Kaggle Open Source Datasets| CSV | https://www.kaggle.com/datasets|
|Australian Bureau of Statistics | REST API, CSV | https://www.abs.gov.au/|
|World Bank Open Data| REST API, CSV | https://data.worldbank.org/|
|Google dataset search| CSV | https://toolbox.google.com/datasetsearch|
|Sample Postgres databases| Database | https://www.postgresql.org/ftp/projects/pgFoundry/dbsamples/| 
|Mock Pizza Kafka Producer | Kafka Producer | https://github.com/aiven/python-fake-data-producer-for-apache-kafka| 

## Timeline 

**Total duration: 2 weeks**

- **28/11/2022**: Provide a project plan 
    - As an individual or in your team, please provide a project plan that includes the following: 
        - Objective of the project (What would you like people to do with the data you have produced?) 
        - Consumers of your data (What users would find your dataset useful?)
        - Datasets your team have selected (What datasets are you sourcing from?)
        - Solution architecture (How does data flow from source to serving?)
        - Breakdown of tasks (How is your project broken down? Who is doing what?)
- **29/11/2022 - 8/12/2022**: Work on your project in class (and outside of class) 
- **12/12/2022**: Project submission 
- **12/12/2022**: 10-15 minute presentation of your project

## Learning objectives 

By the end of this project, you will have hopefully learnt the following: 

1. Working in teams using Git (git commits, push, branching and pull requests)
2. Dividing work effectively between team members in data engineering projects 
3. Apply full or incremental extraction techniques to your data source(s) using a data integration tool
4. Apply full or incremental or upsert loading techniques to your target database or data lake using a data integration tool
5. Apply data transformation and enrichment techniques to your data using a big data transformation tool 
8. Apply logging techniques to enable easy tracking of the pipeline status 
9. Apply streaming techniques to achieve real-time data processing
10. Apply data quality tests to ETL/ELT steps
11. Apply data modelling techniques (e.g. 3NF, dimensional modelling) 
12. Create CI and/or CD pipelines to integrate and deploy application code
13. Deploy the ETL/ELT solution to the cloud 


## Requirements and rubric 

<table>
    <tr>    
        <th>Requirement</th>
        <th>Percentage of marks</th>
    </tr>
    <tr>    
        <td>
            [Batch or Streaming] Use either a static or live dataset. 
            <li>A static dataset refers to a dataset that is not changing e.g. a CSV file.  </li>
            <li>A live dataset refers to a dataset that has data updating live (e.g. every second, every minute, every hour, every day).</li>
            <li>A live dataset can also refer to a dataset that you are able to generate mock data from, for example, a mock kafka producer or a database table.</li>
        </td>
        <td>
            <li>Static dataset: 5%</li>
            <li>Live dataset: 10%</li>
        </td>
    </tr>
    <tr>    
        <td>
            [Batch only] Using a data integration tool (e.g. Airbyte, Fivetran), extract data using either full extract or incremental extract. 
            <li>A full extract refers to a full read of a file, a full read of a database table, or a full read from an API endpoint. </li>
            <li>An incremental extract refers to reading a database table with a filter condition on a timestamp column e.g. `where event_date > '2020-01-01'`, or reading from an API endpoint with a query parameter e.g. `localhost/api?date=2020-01-01`.</li>
        </td>
        <td>
            <li>Full extract: 2.5%</li>
            <li>Incremental extract: 5%</li>
            <li>[Optional] +5% bonus marks for creating a custom airbyte connector</li>
        </td>
    </tr>
    <tr>
        <td>
            [Batch only] Using a data integration tool (e.g. Airbyte, Fivetran), load data to either a data warehouse table or lakehouse table/file using either full load, incremental load, or upsert load. 
            <li>A full load refers to overwriting all records in the target table or file with new records. </li>
            <li>An incremental load refers to inserting only new records to the target table or file.</li>
            <li>An upsert load refers to inserting new records or updating existing records to the target table or file. This is the equivalent of 'incremental - deduped history' in airbyte.</li>
        </td>
        <td>
            <li>Full load: 2.5%</li>
            <li>Incremental load (append only): 3%</li>
            <li>Upsert load (incremental, deduped history): 5%</li>
        </td>
    </tr>
    <tr>    
        <td>
            [Streaming only] Produce events to a kafka topic. Consume events from the kafka topic using a kafka producer of kafka connect. 
            <li>Create or use an existing mock Kafka producer to write to a kafka topic. </li>
            <li>Create a custom kafka consumer, or use an existing kafka connector to consume from a kafka topic. </li>
        </td>
        <td>
            <li>Kafka producer: 5%</li>
            <li>Kafka connect/consumer: 5%</li>
        </td>
    </tr>
    <tr>    
        <td>
            [Batch or streaming] Transform data in batch or real-time using either a Data Warehouse technology (e.g. Databricks Spark, Snowflake, BigQuery, Redshift, Synapse) or a Real-time Database technology (e.g. Clickhouse). Transformations should use the following techniques: 
            <li>Aggregation function e.g. `avg`, `sum`, `max`, `min`, `count`, `rank`</li>
            <li>Grouping i.e. `group by`</li>
            <li>Window function e.g. `partition by`</li>
            <li>Calculation e.g. `column_A + column_B`</li>
            <li>Data type casting</li>
            <li>Filtering e.g. `where`, `having`</li>
            <li>Sorting</li>
            <li>Joins/merges</li>
            <li>Unions</li>
            <li>Renaming e.g. `select col_a as my_col_a` </li>
        </td>
        <td>
            <li>3 transformation techniques: 5%</li>
            <li>5 transformation techniques: 7%</li>
            <li>7 transformation techniques: 10%</li>
        </td>
    </tr>
    <tr>
        <td>
        [Batch only] Apply modelling techniques e.g. Kimball, OBT, Semantic etc. (hint: Fact, Dim, Surrogate Key, SCD2)
        </td>
        <td>
            <li>Basic modelling 5%</li>
            <li>Advanced modelling 10%</li>
        </td>
    </tr>
    <tr>    
        <td>
            [Batch or streaming] Write data quality tests for transformation tasks (e.g. dbt tests, great expectations, soda). For streaming (e.g. clickhouse) you may use <a href="https://clickhouse.com/docs/en/integrations/dbt/dbt-intro">dbt</a> to create views and perform data quality tests on the views. 
        </td>
        <td>
            <li>2 data quality tests: 5% </li>
            <li>5 data quality tests: 10% </li>
        </td>
    </tr>
    <tr>    
        <td>
            [Streaming only] Enable <a href="https://docs.confluent.io/cloud/current/get-started/schema-registry.html">schema registry</a> for your kafka topic and provide a kafka schema.  
        </td>
        <td>
            <li>Schema provided: 10% </li>
        </td>
    </tr>
    <tr>    
        <td>
            [Batch only] Create dependencies between data integration and data transformation tasks. Schedule and monitor tasks using a data orchestration tool (e.g. Airflow, Databricks Workflow). 
        </td>
        <td>
            <li>Dependencies between data integration and data transformation tasks: 2.5%</li>
            <li>+ Monitoring (logs and historical run statuses and duration) and alerting (email or slack notification): 5%</li>
        </td>
    </tr>
    <tr>    
        <td>
            [Batch or streaming] Create a data application that generates insights or predictions for end-users (e.g. a Preset dashboard, a real-time ML application): 
        </td>
        <td>
            <li>Dashboard (e.g. Preset): 10%</li>
            <li>[Optional] Real-time ML model inference: 20%</li>
        </td>
    </tr>
    <tr>    
        <td>
            [Batch or streaming] Deploy solution to Cloud services (provide screenshot evidence of services configured/running where possible): 
            <li>Data integration service (e.g. Airbyte, Fivetran) - screenshot of configured tasks</li>
            <li>Data transformation services (e.g. dbt sql, databricks notebook)</li>
            <li>Data Warehouse (e.g. Snowflake) or Data Lakehouse (e.g. Databricks) depending on your choice</li>
            <li>Data orchestration service (e.g. Airflow, Databricks Workflows) - if you choose Airflow, there is no need to host it on the cloud due to the cost (e.g. MWAA costs $0.50 USD per hour) </li>
            <li>Kafka producer hosted on a cloud service (e.g. ECS service)</li>
            <li>Kafka broker hosted on a cloud service (e.g. Confluent Cloud)</li>
            <li>Kafka connect or consumer hosted on a cloud service (e.g. Confluent Cloud)</li>
            <li>Real-time database hosted on a cloud service (e.g. Clickhouse cloud)</li>
        </td>
        <td>
            Entire solution hosted on cloud services: 15% 
        </td>
    </tr>
    <tr>
        <td>
            [Batch or streaming] Using git for collaboration: 
            <li>Git commits and git push</li>
            <li>Git branching</li>
            <li>Pull request and review</li>
        </td>
        <td>
            <li>Git commits and push only: 2.5%</li>
            <li>+ Git branching: 4%</li>
            <li>+ Pull request and review: 5%</li>
        </td>
    </tr>
    <tr>
        <td>
            [Batch or streaming] Create CI and/or CD pipelines to: 
            <li>CI - build and test code when a pull request is triggered</li>
            <li>CD - build and deploy code to a target environment (e.g. preprod, and prod)</li>
        </td>
        <td>
            <li>CI pipeline with build and tests: 7.5%</li>
            <li>+ CD pipeline with deployment of application code to target environment: 7.5%</li>
        </td>
    </tr>
    <tr>    
        <td>
            Presentation - explain the following: 
            <li>Project context and goals</li>
            <li>Datasets selected</li>
            <li>Solution architecture diagram using <a href="https://www.draw.io/">draw.io</a> or similar. See <a href="https://about.gitlab.com/handbook/business-technology/data-team/platform/#our-data-stack">GitLab's data platform architecture diagram</a> as an example.</li>
            <li>ELT/ETL techniques applied</li>
            <li>Final dataset and demo run</li>
            <li>Insights from your data</li>
            <li>Lessons learnt</li>
        </td>
        <td>
            <li>Project context and goals: 1%</li>
            <li>Datasets selected: 1%</li>
            <li>Solution architecture diagram: 1%</li>
            <li>ELT/ETL techniques applied: 2%</li>
            <li>Final dataset and demo run: 2%</li>
            <li>Insights from your data (e.g. dashboard or machine learning): 2%</li>
            <li>Lessons learnt: 1%</li>
        </td>
    </tr>
    <tr>    
        <td>
            Project structure and documentation
            <li>Clear project structure using a mono-repo approach with folders such as `data transformation`, `data integration`, `data orchestration` for the various components</li>
            <li>Code documentation using <a href="https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings">Python docstrings and comments</a> or SQL comments where reasonable</li>
            <li>README file at the root of the repository explaining the project context, architecture and installation/running instructions. See <a href="https://github.com/matiassingers/awesome-readme">here</a> for examples.</li>
        </td>
        <td>
            <li>Clear project structure: 2.5%</li>
            <li>Code documentation using Python or SQL comments where reasonable: 2.5%</li>
            <li>Detailed markdown documentation explaining the project context, architecture and installation/running instructions: 5%</li>
        </td>
    </tr>
</table>


## Tips

### Project management 
- **Divide and conquer**: Find ways to parallelise the work you do as a team. For example, assuming an EL/T pattern: 
    - Step 1 (In parallel):
        - Person A and B pair program on the Extract and Load pipeline 
        - Person C and D pair program on the Transform pipeline 
    - Step 2 (In parallel):
        - Person A and C pair program on stitching the ELT pipeline together, adding logging and creating the Dockerfile for the docker image 
        - Person B and D pair program on creating the required AWS services (e.g. RDS, ECR, S3, ECS)
    - Step 3 (In parallel):
        - Person A and B pair program on writing unit tests, documentation, and preparing slides for the presentation 
        - Person C and D pair program on deploying the solution to AWS 
- **Don't overthink it**: We're not looking for the perfect solution with every minor detail resolved. It is okay to incur [technical debt](https://www.productplan.com/glossary/technical-debt/) to get to the end goal quickly for the project due to time constraints. In the real world, we would come back later to pay down the technical debt we've incurred by fixing the loose ends. 
- **Stick to the requirements and rubric**: We will be assessing your project based on the requirements in the rubric. Aim to tick off items in the rubric before looking to go beyond the scope. 
- **Give it a good go, but know when to ask for help**: Always have a good go before asking for help as that is the best way you will exercise your problem solving muscles. However, if you find yourself spending more than 20-30 minutes on a single challenging problem, with no clear idea of how you will solve it, then reach out to your teammates or the teaching staff for help. 

### High quality projects
- **Provide a succinct and comprehensive README**: readers of your personal project will always start with the README to know where to begin. The goal of the README is to provide the reader an understanding of the business problem you are trying to solve, how your solution goes about solving it (solution architecture diagram), and how to get started and run your code. There are plenty of great README examples here: https://github.com/matiassingers/awesome-readme

- **Include an architecture diagram in your README to explain the components of your project**: data engineering is a backend role, and there's often not a flashy front-end thing you can show to impress people. Therefore, an architecture diagram is great at giving both technical and non-technical readers an understanding of the solution you've built. Use a tool like https://www.draw.io/ to create your architecture diagrams.

- **Break your project down into components and folders**: technical readers of your project will want to see that you have broken down the project into logical folders so that the code appears organized. There's nothing worse than clicking on a github link and seeing 40 files at the root of the repository and the reader asking themselves "where do I start?". Here is a very basic example: https://github.com/Data-Engineer-Camp/modern-elt-demo

- **Include bells and whistles to impress the reader**: Most projects will have the common things like ETL scripts (e.g. SQL, Python, Airflow, dbt, etc) covered. To go the extra mile and stand out, you should also include things like data quality tests (e.g. dbt tests, great expectations, soda), linting scripts (e.g. sqlfluff, black), CI pipelines that check for linting and unit tests for ETL code before code can be merged to main (e.g. github actions). Include instructions on how to run those tests or linting or CI pipelines in your README file and include screenshots of the success or failure output to give the reader an example of what they should see if they run it themselves.

- **Run it all on the cloud**: Employers these days are also wanting to see data engineers understand how to deploy their solution on the cloud (e.g. AWS, Azure GCP). So try to include (1) cloud services in your solution architecture diagram, and (2) instructions in your README on how to host your ETL solution on a cloud provider. Bonus points if you can script all the infrastructure deployment steps through an Infrastructure as Code (IaC) tool like terraform, but it's not super necessary to know how to do this as most companies would have dedicated cloud engineers to support you with that.

