# Instruction 

## Concept 

Let's learn how to add functionality to support incremental syncs. 

## Task 

### Pass `start_date` into streams 

```python
def streams(self, config: Mapping[str, Any]) -> List[Stream]:
    auth = NoAuth()
    start_date = datetime.strptime(config['start_date'], '%Y-%m-%d')
    return [ExchangeRates(authenticator=auth, config=config, start_date=start_date)]
```

### Modify `ExchangeRates` class 

1. Modify ExchangeRates class to include `cursor_field` as a class variable and in the constructor.
2. Receive `start_date` in the constructor. 

```python 
class ExchangeRates(HttpStream):
    url_base = "https://api.apilayer.com/exchangerates_data/"
    primary_key = "date" 
    cursor_field = "date" # informs the stream that it now supports incremental sync 

    def __init__(self, config: Mapping[str, Any], start_date: datetime, **kwargs):
        super().__init__()
        self.base = config['base']
        self.apikey = config['apikey']
        self.start_date = start_date
        self._cursor_value = None
```

### Create `get_updated_state` method 

This method updates the `state`. The `state` is what is used at the end of each query to keep track of what has just been processed. 

```python
class ExchangeRates(HttpStream):
    ... 
    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, any]:
        # This method is called once for each record returned from the API to compare the cursor field value in that record with the current state
        # we then return an updated state object. If this is the first time we run a sync or no state was passed, current_stream_state will be None.
        if current_stream_state is not None and "date" in current_stream_state:
            current_parsed_date = datetime.strptime(current_stream_state["date"], "%Y-%m-%d")
            latest_record_date = datetime.strptime(latest_record["date"], "%Y-%m-%d")
            return {"date": max(current_parsed_date, latest_record_date).strftime("%Y-%m-%d")}
        else:
            return {"date": self.start_date.strftime("%Y-%m-%d")}
```

### Create `_chunk_date_range` and `stream_slices` 

1. `_chunk_date_range` is an internal method used to obtain a list of dates that needs to be processed. 
2. `stream_slices` is the interface called by airbyte to obtain a list of dates to process. 

```python
class ExchangeRates(HttpStream):
    ... 
    def _chunk_date_range(self, start_date: datetime) -> List[Mapping[str, Any]]: 
        dates = []
        while start_date < datetime.now():
            dates.append({self.cursor_field: start_date.strftime("%Y-%m-%d")})
            start_date += timedelta(days=1)
        return dates 

    def stream_slices(self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any]=None)-> Iterable[Optional[Mapping[str, Any]]]:
        start_date = datetime.strptime(stream_state[self.cursor_field], "%Y-%m-%d") if stream_state and self.cursor_field in stream_state else self.start_date 
        return self._chunk_date_range(start_date)
```

### Update `path` 

Instead of `path` just returning `/latest`, `path` will now need to return a date so that it can be combined with the `base_url` to form something like `https://api.apilayer.com/exchangerates_data/2020-01-01`.

```python
class ExchangeRates(HttpStream):
    ... 
    def path(
        self, 
        stream_state: Mapping[str, Any] = None, 
        stream_slice: Mapping[str, Any] = None, 
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return stream_slice["date"]
```

### Change `sync_mode` in `sample_files/configured_catalog.json`

The `sync_mode` in `sample_files/configured_catalog.json` was originally set to `full_refresh`. 

We'll need to change that to `incremental` for testing purposes. 

### Test the changes 

Test the changes by running: 

```
python main.py read --config secrets/config.json --catalog sample_files/configured_catalog.json
```

### Build the container 
1. Build the connector 

```
docker build . -t airbyte/source-python-http-example:dev
```

2. Go to airbyte (localhost:8000)

3. Select `Settings`

4. Select `Sources`

5. Select `+ New connector` 
  - Display name: `source-python-http-example`
  - Docker repository name: `airbyte/source-python-http-example`
  - Docker image tag: `dev` 
  - Connector documentation url: `https://apilayer.com/marketplace/exchangerates_data-api` 

6. Select `Add` 


### Using the connector 

Go ahead and create a new source and connection using the connector and verify that data is able to be synced to the destination. 


