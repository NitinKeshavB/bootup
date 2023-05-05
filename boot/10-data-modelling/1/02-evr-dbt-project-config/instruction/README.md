# Instruction

## dbt project

The `/solved` folder contains the dbt starting project for this lesson. 

- `dbt_project.yml` has been configured with the appropriate schema names:
    ```yaml
    models:
        adventureworks:
            staging:
            date:
                +materialized: table
                +schema: date
            person: 
                +materialized: table
                +schema: person
            production: 
                +materialized: table
                +schema: production
            purchasing:
                +materialized: table
                +schema: purchasing
            sales: 
                +materialized: table
                +schema: sales
            serving:
            +materialized: table
            +schema: serving  
    ```

- `packages.yml` has been configured with the required libraries. We will run the installation for this later. 

- `profiles.yml` has been configured to point to your localhost instance of postgresql. Please review and update this file if required. 

- `macros/override_default_schema_name.sql` is a macro that overrides the default behaviour of the dbt table naming convention. Instead of `<database_schema>.<schema_name>_<table_name>` it simply does `<schema_name>.<table_name>` for a cleaner naming convention. 

- `models/sources` contains `.yml` sources files for each database schema e.g. `person.yml`, `production.yml`, etc. This will be useful when creating the staging models. 

- `models/staging` contains `.sql` model files for staging models. e.g. `stg_product.sql`. Staging models have a 1:1 relationship to the source models. 

## Getting started 

1. Install python dependencies 

```
pip install dbt-core
pip install dbt-postgres
```

2. Install dbt dependencies 

```
dbt deps 
```

Verify that the installation has ran successfully. 

3. Run and test all dbt models

```
dbt build
```

Verify that the run and test has ran successfully. 

4. Take note of the `staging/stg_date.sql` model. It was created using a dbt package called [dbt_date](https://hub.getdbt.com/calogica/dbt_date/latest/).


5. Generate and render dbt docs 

```
dbt docs generate
dbt docs serve
```

