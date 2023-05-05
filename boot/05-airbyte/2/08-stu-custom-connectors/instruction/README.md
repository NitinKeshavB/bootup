# Instruction

Create a custom connector for the Alpaca markets historical [trades API](https://alpaca.markets/docs/api-references/market-data-api/stock-pricing-data/historical/#trades). 


### Creating the source 

1. Clone the airbyte repo https://github.com/airbytehq/airbyte
2. `cd airbyte-integrations/connector-templates/generator` 
3. `./generate.sh` and select 
    - Python HTTP API Source
    - Provide the name `alpaca-trades` 
4. Review the new source connector template that has been created 

### Install dependencies  

```
cd ../../connectors/alpaca-trades
python -m venv .venv # Create a virtual environment in the .venv directory
conda deactivate # dectivate your conda environment 
source .venv/bin/activate # enable the venv
pip install -r requirements.txt
```

### Define the input parameter  

Airbyte provides a file called `spec.yaml`. This file defines the input parameters that the connector must receive when used. 

Configure `spec.yaml` to the following for exchange rates api: 

```
documentationUrl: https://alpaca.markets/docs/api-references/market-data-api/stock-pricing-data/historical/#trades
connectionSpecification:
  $schema: http://json-schema.org/draft-07/schema#
  title: Alpaca Trades Spec
  type: object
  required:
    - api_key_id
    - api_secret_key
    - symbol
    - start_date
  properties:
    api_key_id:
      type: string
      description: api key id 
    api_secret_key:
      type: string
      description: api secret key 
    symbol:
      type: string
      description: stock symbol
    start_date:
      type: string
      description: start date
```

### Implement `check` operation 

Airbyte uses `SourceAlpacaTrades` as the entrypoint class used for the connector. 

The class needs to implement two methods: 
- `check_connection()`: used by airbyte to check if the connection works 
- `streams()`: used by airbyte to start the stream (aka data extraction or loading)

In `/source_python_http_example/source.py`: 
```python 
class SourceAlpacaTrades(AbstractSource):
    
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        return True, None
```

### Define the schema 

Create class for alpaca trades.

```python
class AlpacaTrades(HttpStream): 
  url_base = "https://data.alpaca.markets/"
  primary_key = "t" 

  def __init__(self, config: Mapping[str, Any], start_date:datetime, **kwargs):
    super().__init__()
    self.api_key_id = config['api_key_id']
    self.api_secret_key = config['api_secret_key']
    self.symbol = config['symbol']
    self.start_date = start_date
```

Set next page token to none: 

```python
class AlpacaTrades(HttpStream): 
  ... 
  def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
    return None         
```

The API endpoint is constructed by combining the `base_url` variable with the value returned from `path()`. 

```python
class ExchangeRates(HttpStream): 
  ...
  def path(
        self, 
        stream_state: Mapping[str, Any] = None, 
        stream_slice: Mapping[str, Any] = None, 
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return f"v2/stocks/{self.symbol}/trades"  
```

Create the request headers used for this request. 

```python
class ExchangeRates(HttpStream): 
  ... 
  def request_headers(
        self,
        stream_state: Mapping[str, Any],
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        return {
            'APCA-API-KEY-ID': self.api_key_id,
            'APCA-API-SECRET-KEY': self.api_secret_key
        }
```

Note: we can also use `request_params` if we need to specify query parameters. 

Implement the `parse_response` method to return JSON to the worker. 

```python
class ExchangeRates(HttpStream): 
  def parse_response(
    self,
    response: requests.Response,
    stream_state: Mapping[str, Any],
    stream_slice: Mapping[str, Any] = None,
    next_page_token: Mapping[str, Any] = None,
  ) -> Iterable[Mapping]:
    return [response.json()]
```

Implement the `stream()` method for the source connector class. The stream is the entrypoint method used to to perform the extraction or loading of data. 

```python
class SourcePythonHttpExample(AbstractSource):
  ...
  def streams(self, config: Mapping[str, Any]) -> List[Stream]:
    # NoAuth just means there is no authentication required for this API and is included for completeness.
    # Skip passing an authenticator if no authentication is required.
    # Other authenticators are available for API token-based auth and Oauth2. 
    auth = NoAuth() 
    return [AlpacaTrades(authenticator=auth, config=config, start_date=start_date)] 
```

Finally, we need to specify the JSON output data that is returned from the connector. Place [alpaca_trades.json](alpaca_trades.json) into the `/source_alpaca_trades/schemas` folder. 

### Test the connector 

#### Create a mock connection 
Create a mock connection configuration using the [configured_catalog.json](configured_catalog.json) file. This file mocks a connection being created in the airbyte user interface. Place that `configured_catalog.json` file into a temporary folder `sample_files` (does not matter the name you decide to give it).

#### Create a secrets file 

Create a `/secrets/config.json` file that contains. 

```json
{
  "api_key_id": "your_key_id",
  "api_secret_key": "your_secret_key",
  "symbol": "tsla"
}
```

This file is only used for testing purposes. 

#### Test the connector 

Test that the connector works locally by running: 
```
python main.py read --config secrets/config.json --catalog sample_files/configured_catalog.json
```


### Use the connector in airbyte 


#### Building and configuring the connector 

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


#### Using the connector 

Go ahead and create a new source and connection using the connector and verify that data is able to be synced to the destination. 

