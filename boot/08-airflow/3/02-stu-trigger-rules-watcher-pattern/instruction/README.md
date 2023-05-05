# Instruction

## Task

Try to implement the same watcher pattern on your own.

Hints:
1. A watcher function outside the DAG, so that you can easily link all tasks to it by `dag.tasks >> watcher()`
2. A failing task that does `bash_command="exit 1"`
3. `from airflow.utils.trigger_rule import TriggerRule` so that you can `trigger_rule=TriggerRule.ONE_FAILED`