# Instruction 

## Concept 

A Dockerfile is used to create a docker image. 

Let's create our own docker image that prints hello world. 

## Implement 

Below is the schema of a Dockerfile. 

`Dockerfile`: 
```docker
FROM <base_image>

WORKDIR <container_working_dir>

COPY <your_dir> <container_dir>

ENV <env_key_1>=<env_value_1>
ENV <env_key_2>=<env_value_2>

RUN <run_any_optional_shell_commands> 

CMD ["python", "<file_name>.py"] # entry point script 
```

Explanation: 
- `FROM`: is used to specify the base image that you will be using. Let's specify `python:3.9` to match the version of python we have been using. 
- `WORKDIR`: is used to specify the working directory in the container.  
- `COPY`: is used to copy files from outside the container (your directory) to the container's working directory. 
- `ENV`: an environment variable if required. 
- `RUN`: is used to run any shell commands e.g. `pip install -r requirements.txt`. 
- `CMD`: is the final run command and calls your entrypoint script. 

See [Dockerfile format docs](https://docs.docker.com/engine/reference/builder/#format) for more. 