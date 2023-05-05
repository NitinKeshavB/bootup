# Instruction 

## Task 

Let's learn how to add functionality to support incremental syncs. 

### Pass `start_date` into streams 

```python
def streams(self, config: Mapping[str, Any]) -> List[Stream]:
    auth = NoAuth()
    start_date = datetime.strptime(config["start_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
    return [AlpacaTrades(authenticator=auth, config=config, start_date=start_date)] 
```

### Modify `AlpacaTrades` class 

1. Modify AlpacaTrades class to include `cursor_field` as a class variable and in the constructor.
2. Receive `start_date` in the constructor. 

```python 
class AlpacaTrades(HttpStream): 
    url_base = "https://data.alpaca.markets/"
    primary_key = "t"
    cursor_field = "t" 

    def __init__(self, config: Mapping[str, Any], start_date:datetime, **kwargs):
        super().__init__()
        self.api_key_id = config['api_key_id']
        self.api_secret_key = config['api_secret_key']
        self.symbol = config['symbol']
        self.start_date = start_date
        self._cursor_value = None
```

### Create `get_updated_state` method 

This method updates the `state`. The `state` is what is used at the end of each query to keep track of what has just been processed. 

```python
class AlpacaTrades(HttpStream):
    ... 
    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]):
        current_stream_state = current_stream_state or {}
        try: 
            current_stream_state[self.cursor_field] = max(
                latest_record["trades"][-1][self.cursor_field], current_stream_state.get(self.cursor_field, self.start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
            )
        except:
            current_stream_state[self.cursor_field] = current_stream_state.get(self.cursor_field, self.start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
        return current_stream_state
```

### Create `_chunk_date_range` and `stream_slices` 

1. `_chunk_date_range` is an internal method used to obtain a list of dates that needs to be processed. 
2. `stream_slices` is the interface called by airbyte to obtain a list of dates to process. 

```python
class AlpacaTrades(HttpStream):
    ... 
    def _chunk_date_range(self, start_date: datetime) -> List[Mapping[str, Any]]:
        """
        Returns a list of each day between the start date and now.
        The return value is a list of dicts {'date': date_string}.
        """
        dates = []
        while start_date < datetime.utcnow():
            dates.append({self.cursor_field: start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')})
            start_date += timedelta(days=1)
        return dates

    def stream_slices(self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any] = None) -> Iterable[Optional[Mapping[str, Any]]]:
        print(f"stream state: {stream_state}")
        start_date = datetime.strptime(stream_state[self.cursor_field], '%Y-%m-%dT%H:%M:%S.%fZ') if stream_state and self.cursor_field in stream_state else self.start_date
        return self._chunk_date_range(start_date)
```

### Add `request_params` 

Add the `request_params` method to return `start` and `end` parameters. 

```python
class ExchangeRates(HttpStream):
    ... 
    def request_params(
            self,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        if datetime.strftime(datetime.strptime(stream_slice['t'], '%Y-%m-%dT%H:%M:%S.%fZ'), "%Y-%m-%d") == datetime.utcnow().strftime("%Y-%m-%d"): 
            return {
                'start': stream_slice['t'],
                'limit': 1
            }
        else: 
            return {
                'start': stream_slice['t'],
                'end': datetime.strftime(datetime.strptime(stream_slice['t'], '%Y-%m-%dT%H:%M:%S.%fZ') + timedelta(days=1), '%Y-%m-%dT%H:%M:%S.%fZ'),
                'limit': 1
            }
```

Note: `limit` is used here for testing purposes only to limit the records returned by the API to 1 record. 

### Change `sync_mode` in `sample_files/configured_catalog.json`

The `sync_mode` in `sample_files/configured_catalog.json` was originally set to `full_refresh`. 

We'll need to change that to `incremental` for testing purposes. 

### Test the changes 

Test the changes by running: 

```
python main.py read --config secrets/config.json --catalog sample_files/configured_catalog.json
```

### Building and configuring the connector 

1. Build the connector 

```
docker build . -t airbyte/source-alpaca-trades:dev
```

2. Go to airbyte (localhost:8000)

3. Select `Settings`

4. Select `Sources`

5. Select `+ New connector` 
  - Display name: `source-alpaca-trades`
  - Docker repository name: `airbyte/source-alpaca-trades`
  - Docker image tag: `dev` 
  - Connector documentation url: `https://alpaca.markets/docs/api-references/market-data-api/stock-pricing-data/historical/#trades`

6. Select `Add` 


### Using the connector 

Go ahead and create a new source and connection using the connector and verify that data is able to be synced to the destination. 

