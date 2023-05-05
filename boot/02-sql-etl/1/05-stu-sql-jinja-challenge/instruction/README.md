# SQL jinja challenge 


## Task 

Challenge: Write a function that processes a model from the `models/` directory. 

After implementing the function, use the function to build all the models in the models directory. 

Hints: 
- create a function that receives a sql file name (without .sql extension), a file path and the database engine 
- check if the sql file exists first. You will have to use `os.listdir("path_to_list")`.
- make use of `logging()` to tell you what function is currently doing 

