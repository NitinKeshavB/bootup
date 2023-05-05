# Instruction
 
## Task
Write a DAG and a task to transform data from Alpaca.
Create `alpaca_etl2.py`.
Complete the `transform` function in `alpaca_functions.py`, it is partially implemented.

```
dags
|-- dag_example
|-- dag_practice
|-- dag_etl
  |-- alpaca_etl1.py
  |-- alpaca_etl2.py
|-- function
  |-- function.py (from previous exercise)
  |-- alpaca_functions.py
```

Checklist:
1. upload exchange codes file to S3
2. have a variable created for the file path
3. task dependency
4. `render_template_as_native_obj`
5. `S3ListOperator`