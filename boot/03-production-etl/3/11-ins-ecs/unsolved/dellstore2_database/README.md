# Instruction (instructor only)

1. Use psql to run a SQL migration script on a postgres database  

    Command: 
    ```
    psql -h <host_name> -d <database_name> -p <port> -U <username> -W -f <filename.sql>
    ```

    Example:
    ```
    psql -h localhost -d dellstore2 -p 5432 -U postgres -W -f dellstore2.sql
    ```

    See [psql usage docs](https://www.postgresql.org/docs/current/app-psql.html)
