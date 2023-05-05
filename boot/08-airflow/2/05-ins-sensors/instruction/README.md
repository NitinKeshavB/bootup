# Instruction

## Concept

### Sensors

Sensors are a special type of Operator.

It waits for something to occur, then succeed so their downstream tasks can run.

Sensors wait for:
- time-based
- waiting for a file
- an external event

Sensors can run in two different modes:
- poke (default): The Sensor takes up a worker slot for its entire runtime 
- reschedule: The Sensor takes up a worker slot only when it is checking, and sleeps for a set duration between checks

All sensors are inherited from `airflow.sensors.base.BaseSensorOperator`
Some key parameters:
```
soft_fail (bool) – Set to true to mark the task as SKIPPED on failure
poke_interval (float) – Time in seconds that the job should wait in between each tries
timeout (float) – Time, in seconds before the task times out and fails.
mode (str) – How the sensor operates. Options are: { poke | reschedule }, default is poke. When set to poke the sensor is taking up a worker slot for its whole execution time and sleeps between pokes. Use this mode if the expected runtime of the sensor is short or if a short poke interval is required. Note that the sensor will hold onto a worker slot and a pool slot for the duration of the sensor’s runtime in this mode. When set to reschedule the sensor task frees the worker slot when the criteria is not yet met and it’s rescheduled at a later time. Use this mode if the time before the criteria is met is expected to be quite long. The poke interval should be more than one minute to prevent too much load on the scheduler.
exponential_backoff (bool) – allow progressive longer waits between pokes by using exponential backoff algorithm
```

# Dynamic Task Mapping
Create a number of tasks at runtime based upon current data, rather than knowing in advance how many tasks would be needed.

```
Operator.partial(
    task_id="xxxx",
    other_shared_parameters="yyyyy"
).expand(
    parameters_to_split=["give", "me", "a", "list", "or", "a", "dict"]
)
```
The scheduler translates this into 7 tasks.

This is somewhat like a for-loop that iterates through the list or dict.

### Task

Use `S3KeySensor` to verify the resulting files of extract and transform.

