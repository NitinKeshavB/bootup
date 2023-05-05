# Instruction

## Concept

### TaskFlow

Define DAGs and tasks using decorators `@dag` and `@task`.

Define flow using Python
```
order_data = extract()
order_summary = transform(order_data)
load(order_summary["total_order_value"])
```

Pros: can be intuitive if all your operators are from the `airflow.operators.python` package
Cons: can be super confusing when mixed with the traditional style operators

## Task

Refactor the DAG to adopt the Taskflow style.
