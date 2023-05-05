# Instruction

## Task 

Create a docker compose file to easily run your containers. 

```yaml
# docker-compose.yml 
version: "3"
services: 
  TODO: 
    image: TODO
    container_name: TODO
    ports: 
      - TODO
    environment:
      - TODO
  
  TODO:
    image: TODO
    depends_on: 
      - TODO 
    environment:
      - TODO
```

## Optional reading 

Use docker secrets with docker compose: 
- [Creating docker secrets](https://docs.docker.com/engine/reference/commandline/secret_create/)
- [Use docker secrets with docker compose](https://www.rockyourcode.com/using-docker-secrets-with-docker-compose/)

