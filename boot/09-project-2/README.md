# Project 2

## Context 

Over the past 4 weeks, you have learnt: 
- How to build data integration pipelines (extract load) using data integration tools like Airbyte
- How to use cluster compute engines to transform data i.e. Snowflake and Databricks (Spark) 
- How to orchestrate data integration and data transformation pipelines using a data orchestration tool like Airflow or Databricks Workflows 
- How to use git to commit code and collaborate with teams using branches 
- How to package and host the various components on Amazon Web Services (AWS) using services such as ECS, ECR, S3, RDS, IAM, EC2, MWAA 

## Goal

- Work in a team to create a big data ETL pipeline using patterns and concepts covered previously. 
- Your big data ETL pipeline should serve the goal of providing useful information to end users such as a data analyst or data scientist. 
- Your data pipeline must have the potential to scale to handle terrabytes or petabytes of data through scale-out cluster compute (e.g. Databricks Spark or Snowflake). However, for the purposes of the project, you are not required to use terrabyte or petabyte size datasets. 
- You may choose any dataset(s) that you and your team would like to work with. For example, you may choose a dataset based on your team's personal or professional interests, or based on the availability and accessibility to data. 
- Your ETL pipeline should have data quality tests and logging. 
- Deploy and schedule your ETL pipeline on the cloud (as much as possible). 
- Present and demo your working solution to the class. 

Here are some data sources (this is not an extensive list and you are encouraged to do your own research): 

|Data source name|URL|
|--|--|
|Public APIs|https://github.com/public-apis/public-apis| 
|Australian Government Open Source Datasets| https://data.gov.au/| 
|Kaggle Open Source Datasets|https://www.kaggle.com/datasets|
|Australian Bureau of Statistics |https://www.abs.gov.au/|
|World Bank Open Data|https://data.worldbank.org/|
|Google dataset search|https://toolbox.google.com/datasetsearch|
|Sample Postgres databases|https://www.postgresql.org/ftp/projects/pgFoundry/dbsamples/| 

## Timeline 

**Total duration: 3 weeks**

- **31/10/2022**: Provide a project plan 
    - Project plan should include: 
        - Objective of the project (What would you like people to do with the data you have produced?) 
        - Consumers of your data (What users would find your dataset useful?)
        - Datasets your team have selected (What datasets are you sourcing from?)
        - Solution architecture (How does data flow from source to serving?)
        - Breakdown of tasks (How is your project broken down? Who is doing what?)
- **01/11/2022 - 03/11/2022**: Work on your project in class (and outside of class) 
- **07/11/2022 - 17/11/2022**: Work on your project outside of class 
- **21/11/2022**: Project submission 
- **21/11/2022**: 7 minute presentation of your project

## Learning objectives 

By the end of this project, you will have hopefully learnt the following: 

1. Working in teams using Git (git commits, push, branching and pull requests)
2. Dividing work effectively between team members in data engineering projects 
3. Apply full or incremental extraction techniques to your data source(s) using a data integration tool
4. Apply full or incremental or upsert loading techniques to your target database or data lake using a data integration tool
5. Apply data transformation and enrichment techniques to your data using a big data transformation tool 
8. Apply logging techniques to enable easy tracking of the pipeline status 
9. Apply data quality tests to ETL/ELT steps 
10. Deploy the ETL/ELT solution to the cloud 


## Requirements and rubric 

<table>
    <tr>    
        <th>Requirement</th>
        <th>Percentage of marks</th>
    </tr>
    <tr>    
        <td>
            Extract data from either a static or live dataset. 
            <li>A static dataset refers to a dataset that is not changing e.g. a CSV file.  </li>
            <li>A live dataset refers to a dataset that has data updating periodically (e.g. every day, every hour, every minute).</li>
            <li>A live dataset can also refer to a dataset that you have full control over (e.g. a database table) and can manually insert data into the database table to mimic a live dataset.</li>
        </td>
        <td>
            <li>Static dataset: 5%</li>
            <li>Live dataset: 10%</li>
        </td>
    </tr>
    <tr>    
        <td>
            Using a data integration tool (e.g. Airbyte, Fivetran), extract data using either full extract or incremental extract. 
            <li>A full extract refers to a full read of a file, a full read of a database table, or a full read from an API endpoint. </li>
            <li>An incremental extract refers to reading a database table with a filter condition on a timestamp column e.g. `where event_date > '2020-01-01'`, or reading from an API endpoint with a query parameter e.g. `localhost/api?date=2020-01-01`.</li>
        </td>
        <td>
            <li>Full extract: 5%</li>
            <li>Incremental extract: 10%</li>
            <li>[Optional] +10% bonus marks for creating a custom airbyte connector</li>
        </td>
    </tr>
    <tr>    
        <td>
            Using a data integration tool (e.g. Airbyte, Fivetran), load data to either a data warehouse table or lakehouse table/file using either full load, incremental load, or upsert load. 
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
            Transform data using big data techonologies (i.e. Databricks Spark or Snowflake). Transformations should use the following techniques: 
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
            Create dependencies between transformation tasks (e.g. DBT, Airflow, Databricks Workflow). 
        </td>
        <td>
            Dependencies between transformation tasks: 5%
        </td>
    </tr>
    <tr>    
        <td>
            Write data quality tests for transformation tasks (e.g. dbt tests, great expectations, soda)
        </td>
        <td>
            <li>2 data quality tests: 5% </li>
            <li>5 data quality tests: 10% </li>
        </td>
    </tr>
    <tr>    
        <td>
            Create dependencies between data integration and data transformation tasks. Schedule and monitor tasks using a data orchestration tool (e.g. Airflow, Databricks Workflow). 
        </td>
        <td>
            <li>Dependencies between data integration and data transformation tasks: 5%</li>
            <li>+ Monitoring (logs and historical run statuses and duration) and alerting (email or slack notification): 10%</li>
        </td>
    </tr>
    <tr>
        <td>
            Using git for collaboration: 
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
            Deploy solution to Cloud services (provide screenshot evidence of services configured/running): 
            <li>Data integration service (e.g. Airbyte, Fivetran) - screenshot of configured tasks</li>
            <li>Data transformation services (e.g. dbt sql, databricks notebook)</li>
            <li>Data Warehouse (e.g. Snowflake) or Data Lakehouse (e.g. Databricks) depending on your choice</li>
            <li>Data orchestration service (e.g. Airflow, Databricks Workflows) - if you choose Airflow, there is no need to host it on the cloud due to the cost (e.g. MWAA costs $0.50 USD per hour) </li>
        </td>
        <td>
            Entire solution hosted on cloud services: 15% 
        </td>
    </tr>
    <tr>    
        <td>
            Presentation - explain the following: 
            <li>Project context and goals</li>
            <li>Datasets selected</li>
            <li>Solution architecture diagram using <a href="https://www.draw.io/">draw.io</a> or similar. See <a href="https://about.gitlab.com/handbook/business-technology/data-team/platform/#our-data-stack">GitLab's data platform architecture diagram</a> as an example.</li>
            <li>ELT/ETL techniques applied</li>
            <li>Final dataset and demo run (if possible)</li>
            <li>Lessons learnt</li>
        </td>
        <td>
            <li>Project context and goals: 1%</li>
            <li>Datasets selected: 1%</li>
            <li>Solution architecture diagram: 2%</li>
            <li>ELT/ETL techniques applied: 2%</li>
            <li>Final dataset and demo run (if possible): 2%</li>
            <li>Lessons learnt: 2%</li>
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

