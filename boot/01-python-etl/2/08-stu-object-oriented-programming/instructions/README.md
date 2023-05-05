# Object oriented programming

Now it is your turn! 

## Task:
- Refactor your python file from the previous exercises into logical structures using object oriented programming.

Your project folder should look similar to this: 

```
src/                                            # the root folder where all our source code sits 
|__ set_python_path.sh                          # a shell helper function that sets our Python Path

|__ database/
    |__ __init__.py
    |__ postgres.py 

|__ other_common_modules/* 

|__ project_name/                               # for example 'weather'
    |__ __init__.py 
    |__ config.sh                               # for setting any environment variables (a.k.a. secret variables) 
    |__ data/*                                  # contains any data files used by the ETL that don't change very often 
    |__ etl/
        |__ __init__.py
        |__ extract.py
        |__ transform.py
        |__ load.py
    |__ pipeline/
        |__ __init__.py
        |__ pipeline.py

```

Be sure to use Python `Class` and `@staticmethod` for your functions within the classes to make the functions callable without creating an object. 


To run your code, make sure you execute the following: 

```
# 1. change directory to the src folder. 
cd your_path_to_src_folder/src

# 2. set the python path. You will only need to do this once. 
. ./set_python_path.sh

# 3. Set the environment variables. You will only need to do this once. 
. ./weather/config.sh 

# 4. Run your python pipeline 
python weather/pipeline/your_pipeline.py

```


