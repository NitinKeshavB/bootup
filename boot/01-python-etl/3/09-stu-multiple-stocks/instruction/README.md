# Dynamic date config 

Now that we have seen how metadata configuration can help us dynamically set logic within our pipeline, let's take it even further and execute our ETL on not just one stock, but multiple stocks that the end user chooses! 

## Task 

1. Configure your YAML file to contain lists for each stock. Use the following stock tickers as a test: 
    - `aapl`: for apple 
    - `amzn`: for amazon 
    - `tsla`: for tesla 

Example of how to refactor the YAML: 

```
# nesting key value pairs and lists 
persons:
    - person: 
        name: Martin D'vloper
        job: Developer
    
    - person: 
        name: Bob D'engineer
        job: Data engineer
```

2. You will need to refactor your code such that `pipeline()` now calls a child pipeline e.g. `pipeline_per_stock()` that executes for each stock ticker. 



