# Instruction

## Steps

1. Create a new github repo and push the files in `solved/` to the new repo. Do not push the `solved` folder itself, but rather the folders underneath it. 

1. Export or set the following variables of your RDS instance to your local machine: 
    ```
    # export for macOS 
    export DB_HOST=your_host_name
    export DB_PASSWORD=your_password
    # set for windows 
    set DB_HOST=your_host_name
    set DB_PASSWORD=your_password
    ```

1. Create a new conda environment e.g. `conda create -n dbt python=3.8` and install requirements.txt `pip install -r requirements.txt`. Activate your new environment `conda activate dbt`.  

1. Perform a dbt run to materialize models into your target using the command `dbt run --target prod` 

1. Check that the `serving` tables have been created successfully. 

