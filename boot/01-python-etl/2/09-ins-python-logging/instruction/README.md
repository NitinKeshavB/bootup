# Python Logging 

## Concept 

Now that we have a good structure going, let's look at a concept that will prove very helpful when we are looking to run our ETL jobs in production, and that is logging. 

Because we have moved away from Jupyter Notebooks, we are not able to interactively understand what is going on with our code anymore. One way to achieve this is to use lots of python `print()` statements in our python file. 

But there is a better way, and that is to use python `logging()`. Logging offers us features such as being able to control different levels of printing e.g. WARNING, ERROR, INFO, and also print a neatly formatted message into the terminal, that looks something like: 

```
[INFO][2022-05-18 20:02:31,956][weather_pipeline.py]: Commencing extract
[INFO][2022-05-18 20:02:36,527][weather_pipeline.py]: Extract complete
[INFO][2022-05-18 20:02:36,527][weather_pipeline.py]: Commencing extract from city csv
[INFO][2022-05-18 20:02:36,530][weather_pipeline.py]: Extract complete
[INFO][2022-05-18 20:02:36,530][weather_pipeline.py]: Commencing transform
[INFO][2022-05-18 20:02:36,537][weather_pipeline.py]: Transform complete
[INFO][2022-05-18 20:02:36,537][weather_pipeline.py]: Commencing load to file
[INFO][2022-05-18 20:02:36,616][weather_pipeline.py]: Load complete
[INFO][2022-05-18 20:02:36,645][weather_pipeline.py]: Commencing load to database
[INFO][2022-05-18 20:02:36,772][weather_pipeline.py]: Load complete
```

## Implementation 

We are going to use the Python [Logging](https://docs.python.org/3/library/logging.html) module. Have a look at the docs. 

There are different levels we can log information for, which the docs will explain further: 
- debug
- info
- warning
- error 
- critical 

We can easily log a statement, similar to `print()` by doing: 

```python
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything unless the configured logging level is changed 
```

We can change the logging level to also print `INFO` logs by doing: 

```python
import logging 
logging.basicConfig(level=logging.INFO)
```

We can output logs easily to a file by doing: 

```python
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
```

We can format the output format of our logs by doing: 

```python
logging.basicConfig(format="[%(levelname)s][%(asctime)s][%(filename)s]: %(message)s") 
```

Note: to see a full list of formats look at the log record attributes [here](https://docs.python.org/3/library/logging.html#logging.LogRecord).

