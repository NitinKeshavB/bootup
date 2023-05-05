# Instruction 

## Set up 

1. Create two new ECR: 
    - adventureworks-dbt-preprod
    - adventureworks-dbt-prod

2. Create one new ECS cluster: 
    - dbt-cluster

3. Create two new ECS task definitions: 
    - dbt-preprod
    - dbt-prod

## Implement CI pipeline 

1. Build 
    - build docker image 
    - push docker image to ECR (preprod and prod)

2. Preprod deploy
    - update and deploy preprod task definition to use new image tag and set environment variables
    - run the ECS task and check for a successful exit 

3. Prod deploy
    - update and deploy prod task definition to use new image tag and set environment variables
    - run the ECS task and check for a successful exit 
