# Instruction 

## Concept 

Similar to Docker Hub Repositories which we learnt in the previous lesson, we can push docker images that we have built to AWS Elastic Container Registry. The benefit of ECR is that the repository is private and integrates well with other AWS services such as Elastic Container Service which we are going to use later. 

## Implement 

### Create ECR 

1. Search for "ECR" in the AWS Console 
2. Select "Create repository":
    - Visibility settings: `Private`
    - Repository name: `"provide_name_here"`
3. Select "Create repository"


### Configure Dockerfile 

1. Move all `ENV` variables into the Dockerfile. 

    Note: This is not ideal as we are storing secrets in plaintext files that are push to a GitHub repository. However, let's keep things simple for now. We'll look at how to store environment secrets safely later on. 

2. Update the `server_name` variables to the RDS hostname. 

### Build and push image 

1. Retrieve an authentication token and authenticate your Docker client to your registry.
    
    Use the AWS CLI:
    ```
    aws ecr get-login-password --region <your_region> | docker login --username AWS --password-stdin <your_ecr_uri> 
    ```

    Note: The above command assumes you have already logged in to AWS CLI using `aws configure`. 

2. Build your Docker image using the following command.

    ```
    docker build . -t dellstore 
    ```

3. Tag your docker image. 
    
    ```
    docker tag dellstore:latest <your_ecr_uri>/dellstore:latest
    ```

4. Push your docker image. 

    ```
    docker push <your_ecr_uri>/dellstore:latest
    ```

