# Instruction

## Task

Now it's your turn!

1. create and upload env file to s3
2. add the profile file to the dbt project
3. create a folder named `docker` directly under `06-snowflake-dbt` to house `dockerfile` and `run_commands.sh`
4. create and push image
5. create task execution role, [add inline policy to access s3](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html)
6. create an ec2 task (remember to set environment file and cloudwatch logs)

For details on ECS task creation, refer to the instructions in Airbyte day 3 content.

Observe:
1. Tables are updated
2. How profile and target works
3. How variables are redacted in the logs
