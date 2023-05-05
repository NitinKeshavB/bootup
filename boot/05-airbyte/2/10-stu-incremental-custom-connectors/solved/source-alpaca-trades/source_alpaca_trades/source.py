#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator
from airbyte_cdk.sources.streams.http.auth import NoAuth
from datetime import * 

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
    
    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]):
        current_stream_state = current_stream_state or {}
        try: 
            current_stream_state[self.cursor_field] = max(
                latest_record["trades"][-1][self.cursor_field], current_stream_state.get(self.cursor_field, self.start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
            )
        except:
            current_stream_state[self.cursor_field] = current_stream_state.get(self.cursor_field, self.start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
        return current_stream_state


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


    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        # The API does not offer pagination, so we return None to indicate there are no more pages in the response
        return None

    def path(
        self, 
        stream_state: Mapping[str, Any] = None, 
        stream_slice: Mapping[str, Any] = None, 
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return f"v2/stocks/{self.symbol}/trades"  
    
    def request_params(
            self,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        print(datetime.strftime(datetime.strptime(stream_slice['t'], '%Y-%m-%dT%H:%M:%S.%fZ'), "%Y-%m-%d"))
        print(datetime.utcnow().strftime("%Y-%m-%d"))
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

    def parse_response(
        self,
        response: requests.Response,
        stream_state: Mapping[str, Any],
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> Iterable[Mapping]:
        return [response.json()]

# Source
class SourceAlpacaTrades(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        """
        TODO: Implement a connection check to validate that the user-provided config can be used to connect to the underlying API

        See https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-stripe/source_stripe/source.py#L232
        for an example.

        :param config:  the user-input config object conforming to the connector's spec.yaml
        :param logger:  logger object
        :return Tuple[bool, any]: (True, None) if the input config can be used to connect to the API successfully, (False, error) otherwise.
        """
        return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        """
        TODO: Replace the streams below with your own streams.

        :param config: A Mapping of the user input configuration as defined in the connector spec.
        """
        auth = NoAuth()
        start_date = datetime.strptime(config["start_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
        return [AlpacaTrades(authenticator=auth, config=config, start_date=start_date)] 

