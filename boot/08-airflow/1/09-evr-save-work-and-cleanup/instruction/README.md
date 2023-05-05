# Instruction

## Task

- Find container id: `docker ps`

- Bash into the running container: `docker exec -it <container_id> bash`

- Save and restore connections:
  1. To save connections into a json: bash into the container, be at the `dags` folder, `airflow connections export --file-format json conns.json`
  2. To restore connections from a json: bash into the container, `airflow connections import conns.json`

- Save and restore variables: use UI.

- Stop the container: either use Docker Desktop or `docker stop <container_id>`

- Avoid issues starting next time, clean up the airflow folder, **REMAIN** only the `dags` folder

