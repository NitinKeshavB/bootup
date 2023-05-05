# Python unit test

Now it is your turn! 

## Task:
1. Create unit tests for your `transform()` and `generate_datetime_ranges()` function. 

Use the following code snippets to create your test file: 

#### Assemble
```python
# assemble 
df_input = pd.DataFrame({
    "name": ["perth", "sydney"],
    "dt": [1657982968, 1657984968],
    "id": [1, 2],
    "main.temp": [27, 21]
})

df_input_population = pd.DataFrame({
    "city_name": ["perth", "sydney"],
    "population": [20000000, 60000000]
})

df_expected = df_expected = pd.DataFrame({
    "datetime": [1657982968, 1657984968],
    "id": [1, 2],
    "name": ["perth", "sydney"],
    "temperature": [27, 21],
    "population": [20000000, 60000000],
    "unique_id": ["16579829681", "16579849682"]
}).set_index("unique_id")
df_expected["datetime"] = pd.to_datetime(df_expected["datetime"], unit="s")
```

#### Act
```python
# act 
df_output = Transform.transform(df=df_input, df_population=df_input_population)
```

#### Assert
```python
# assert 
pd.testing.assert_frame_equal(left=df_output, right=df_expected,check_exact=True)
```

Remember to: 
- create a python file with test_ prefixed or _test postfixed to the name of the file.
- write a function that asserts a condition, with test_ prefixed or _test postfixed to the end of the function name. 

