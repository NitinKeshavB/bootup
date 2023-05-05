from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator
from airbyte_cdk.sources.streams.http.auth import NoAuth
from datetime import * 

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

    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, any]:
        # This method is called once for each record returned from the API to compare the cursor field value in that record with the current state
        # we then return an updated state object. If this is the first time we run a sync or no state was passed, current_stream_state will be None.
        if current_stream_state is not None and "date" in current_stream_state:
            current_parsed_date = datetime.strptime(current_stream_state["date"], "%Y-%m-%d")
            latest_record_date = datetime.strptime(latest_record["date"], "%Y-%m-%d")
            return {"date": max(current_parsed_date, latest_record_date).strftime("%Y-%m-%d")}
        else:
            return {"date": self.start_date.strftime("%Y-%m-%d")}

    def _chunk_date_range(self, start_date: datetime) -> List[Mapping[str, Any]]: 
        dates = []
        while start_date < datetime.now():
            dates.append({self.cursor_field: start_date.strftime("%Y-%m-%d")})
            start_date += timedelta(days=1)
        return dates 

    def stream_slices(self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any]=None)-> Iterable[Optional[Mapping[str, Any]]]:
        start_date = datetime.strptime(stream_state[self.cursor_field], "%Y-%m-%d") if stream_state and self.cursor_field in stream_state else self.start_date 
        return self._chunk_date_range(start_date)

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        # this api does not offer pagination, so we return None to indicate that there are no more pages 
        return None         
    
    def path(
        self, 
        stream_state: Mapping[str, Any] = None, 
        stream_slice: Mapping[str, Any] = None, 
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        # The "/latest" path gives us the latest currency exchange rates
        # return "latest"
        return stream_slice["date"]

    def request_headers(
            self,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        # The api requires that we include apikey as a header
        return {'apikey': self.apikey}

    def parse_response(
            self,
            response: requests.Response,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> Iterable[Mapping]:
        # The response is a simple JSON whose schema matches our stream's schema exactly, 
        # so we just return a list containing the response
        return [response.json()]

    def stream_slices(
        self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any] = None
    ) -> Iterable[Optional[Mapping[str, any]]]:
        start_date = datetime.strptime(stream_state["date"], "%Y-%m-%d") if stream_state and "date" in stream_state else self.start_date
        return self._chunk_date_range(start_date)
    


class SourcePythonHttpExample(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        """
        TODO: Implement a connection check to validate that the user-provided config can be used to connect to the underlying API

        See https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-stripe/source_stripe/source.py#L232
        for an example.

        :param config:  the user-input config object conforming to the connector's spec.yaml
        :param logger:  logger object
        :return Tuple[bool, any]: (True, None) if the input config can be used to connect to the API successfully, (False, error) otherwise.
        """
        accepted_currencies = {"USD", "JPY", "BGN", "CZK", "DKK"}
        input_currency = config["base"]
        if input_currency not in accepted_currencies:
            return False, f"Input currency '{input_currency}' is not valid. Please input one of the following {accepted_currencies}"
        else: 
            return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        # NoAuth just means there is no authentication required for this API and is included for completeness.
        # Skip passing an authenticator if no authentication is required.
        # Other authenticators are available for API token-based auth and Oauth2. 
        auth = NoAuth()  
        start_date = datetime.strptime(config['start_date'], '%Y-%m-%d')
        return [ExchangeRates(authenticator=auth, config=config, start_date=start_date)]
