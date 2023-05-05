# Data Engineer Camp 
![python](https://img.shields.io/badge/python-lang-red)
![sql](https://img.shields.io/badge/sql-lang-red)
![bash](https://img.shields.io/badge/bash-lang-red)
![airbyte](https://img.shields.io/badge/snowflake-tool-blue)
![snowflake](https://img.shields.io/badge/snowflake-tool-blue)
![databricks](https://img.shields.io/badge/databricks-tool-blue)
![spark](https://img.shields.io/badge/spark-tool-blue)
![dbt](https://img.shields.io/badge/dbt-tool-blue)
![airflow](https://img.shields.io/badge/spark-tool-blue)
![preset](https://img.shields.io/badge/preset-tool-blue)
![kafka](https://img.shields.io/badge/kafka-tool-blue)
![druid](https://img.shields.io/badge/druid-tool-blue)
![git](https://img.shields.io/badge/git-tool-blue)
![github-actions](https://img.shields.io/badge/ghactions-tool-blue)
![docker](https://img.shields.io/badge/docker-tool-blue)
![aws](https://img.shields.io/badge/aws-tool-blue)

## Welcome 

Welcome to the Data Engineer Camp bootcamp repo. The bootcamp is designed to help aspiring data engineers gain the skills to become a proficient data engineer with the modern data stack. 


## Repository structure 

Please read this section to understand how to navigate the repository. 

The contents of the repository is broken down as follows: 

```
root 
|__ <week_num>-<topic_title>
    |__ <lesson_num>
        |__ <activity_num>-<activity_type>-<activity_title>
            |__ instruction/README.md
            |__ solved/*
            |__ unsolved/*
```

- `week_num`: refers to the week number e.g. 01, 02, 03. 
- `topic_title`: refers to the week's topic e.g. Python ETL, SQL ETL. 
- `lesson_num`: refers to the lesson number i.e. 1 or 2 or 3. 
- `activity_num` : refers to the activity number e.g. 01, 02, 03. 
- `activity_type`: refers to the activity type i.e. [`ins`] instructor, [`stu`] student, [`evr`] everyone. 
- `activity_title`: refers to the activity title e.g. Extracting data, transforming data. 

Example: 
```
root 
|__ 01-python-etl
    |__ 1
        |__ 03-ins-extracting-data
            |__ instruction/README.md
            |__ solved/*
            |__ unsolved/*
        |__ 04-stu-extracting-data
            |__ instruction/README.md
            |__ solved/*
            |__ unsolved/*
```


Each activity contains the following folders: 
- `instruction`: contains a `README.md` file along with other files related to the instruction for the activity. 
- `solved`: contains the solved solutions for the activity. [`stu`] solved solutions will be uploaded at the end of each class. 
- `unsolved`: contains the unsolved starting code for the activity. This folder may be empty at times if the code is to be created from scratch. 

