# Instruction

Create a docker image for the ETL application.

## Task 

1. Write the Dockerfile 

    Note: secret environment variables should be kept in a `.env` file.  

2. Create the `.env` file to store secret environment variables 

3. Build the docker image 

    ```
    docker build . -t <name_of_your_tag>
    ```

4. Run the docker image 

    ```
    docker run --rm --env-file .env <image_name>
    ```


