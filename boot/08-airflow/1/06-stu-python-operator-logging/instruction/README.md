# Instruction

## Task
To get some simple hands-on before we write our ETL DAG.

```
dags
|-- dag_example
|-- dag_practice
  |-- my_first_dag_stu.py 
|-- function
  |-- function.py
```
1. Create `my_first_dag_stu.py` and `function.py` at the location shown above.
2. In `function.py`
   1. implement 3 functions, each one takes 1 string argument
   2. use `logging` to log this string at `warning`, `info` and `debug` level respectively in different functions
3. In `my_first_dag.py`
   1. author a DAG that's scheduled once a day at 6am UTC time
   2. the DAG starts from yesterday and no catchup
   3. use the `PythonOperator` 3 times to call the 3 functions once each
   4. make the 3 tasks log the start of `data_interval` (hint: use jinja template)
   5. chain the 3 tasks to run from the highest severity to the lowest
4. Enable your DAG and see what gets logged at what level