# Instruction

## Task 

### Create ECR 

1. Search for "ECR" in the AWS Console 
2. Select "Create repository":
    - Visibility settings: `Private`
    - Repository name: `"provide_name_here"`
3. Select "Create repository"


### Build and push image to ECR 

Build an image from the student containerise activity from the previous lesson. 

1. Retrieve an authentication token and authenticate your Docker client to your registry.
    
    Use the AWS CLI:
    ```
    aws ecr get-login-password --region <your_region> | docker login --username AWS --password-stdin <your_ecr_uri> 
    ```

    Note: The above command assumes you have already logged in to AWS CLI using `aws configure`. 

2. Build your Docker image using the following command.

    ```
    docker build . -t dvd_rental 
    ```

3. Tag your docker image. 
    
    ```
    docker tag dvd_rental:latest <your_ecr_uri>/dvd_rental:latest
    ```

4. Push your docker image. 

    ```
    docker push <your_ecr_uri>/dvd_rental:latest
    ```
