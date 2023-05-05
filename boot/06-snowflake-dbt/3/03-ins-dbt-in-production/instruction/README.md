# Instruction

## Concept

### dbt in Production
Running dbt in production simply means setting up a system to run a dbt job on a schedule, rather than running dbt commands manually from the command line.

It sounds simple, but there are a few considerations:
- The complexity involved in creating a new dbt job, or editing an existing one.
- Setting up notifications if a step within your job returns an error code (e.g. a model cannot be built, or a test fails).
- Accessing logs to help debug any issues.
- Pulling the latest version of your git repo before running dbt (i.e. continuous deployment).
- Running your dbt project before merging code into master (i.e. continuous integration).
- Allowing access for team members that need to collaborate on your dbt project.

Common ways to run dbt in production:
- dbt Cloud (it is free for one developer's personal use)
- Airflow
- Perfect/Dagster
- Automation Server: Bamboo, Jenkins, Gitlab CI/CD, AWS CodeDeploy
- Good old cron job

### profiles.yml, Targets and Separated Environments

A profile consists of targets, and a specified default target.

Profile file is usually `~/.dbt/profiles.yml`  e.g. `C:\Users\MYNAME\.dbt\profiles.yml`

To use a specific profile file:
- `dbt run --profiles-dir path/to/directory` or
- `export DBT_PROFILES_DIR=path/to/directory`

A typical profile when using dbt locally (i.e. running from your command line) will have a target named dev, and have this set as the default.

```yaml
decdotcom:
  outputs:
    dev:
      account: jb64263.ap-southeast-2
      database: HR
      password: iwonttellyou
      role: DBT_RW
      schema: MODEL
      threads: 1
      type: snowflake
      user: dbt
      warehouse: ETL
  target: dev
```
Targets offer the flexibility to decide how to implement your separate environments

To use environmental variables in profiles.yml: `{{ env_var('DBT_PASSWORD') }}`

To safely use environmental variables in profiles.yml: prefix your envvar with `DBT_ENV_SECRET_`, this
- restricts usage to profiles.yml + packages.yml
- will be scrubbed from dbt logs and replaced with *****

### `dbt build`
The dbt build command will:

- run models
- test tests
- snapshot snapshots
- seed seeds

in DAG order. But it does not install deps!

Note that Tests on upstream resources will block downstream resources from running, and a test failure will cause those downstream resources to skip entirely.

To avoid skipping, adjust tests' severity to `warn` instead of `error` (Test specific config)

## Task

1. create and upload env file to s3
2. add the profile file to the dbt project
3. create a folder named `docker` directly under `06-snowflake-dbt` to house `dockerfile` and `run_commands.sh`
4. create and push image
5. create task execution role, [add inline policy to access s3](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html)
6. create an ec2 task (remember to set environment file and cloudwatch logs)

We are baking the code repo into the images. This is something to be improved. It is a better approach to fetch the code on the fly.