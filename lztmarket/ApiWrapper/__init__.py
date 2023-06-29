import logging
import time
from .ApiExceptions import TimeLimitReached, ApiError

import httpx


logging.basicConfig(
    format="%(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s")


class Wrapper:
    """Class for sending requests to the server.
    """
    _last_request_timestamp = None

    def __init__(self, api_key: str) -> None:
        """
        Creates a new instance of the Wrapper class.

        Args:
        api_key (str): the API key for authentication on the server.
        """

        logging.debug("New instance of Wrapper created.")
        self._api_key = api_key
        self._end_point = "https://api.lzt.market"
        self.client = httpx.AsyncClient()

    def __ip_block_protect(func):
        async def wrapper(self, *args, **kwargs):
            if not self.can_send:
                raise TimeLimitReached(
                    "You cannot send a request at this time, as it will lead to a blocking of your ip address. "
                    "Please wait. Use the 'can_send' attribute to check if the request can be sent.")
            Wrapper._last_request_timestamp = int(time.time())
            return await func(self, *args, **kwargs)
        return wrapper

    @property
    def can_send(self) -> bool:
        return not (Wrapper._last_request_timestamp and int(time.time()) - Wrapper._last_request_timestamp < 4)

    @__ip_block_protect
    async def _execute(self, path: str, method: str, params: dict = None, data: str = None):
        """Executes an HTTP request to the specified endpoint and returns the response as a JSON object.

        Args:
            path (str): The path component of the URL.
            method (str): The HTTP method to use for the request (e.g., GET, POST, PUT, DELETE).
            params (dict, optional): A dictionary of query parameters to include in the request URL.
            data (str, optional): The request body as a string.

        Returns:
            The response from the HTTP request as a JSON object.
        """
        HEADERS = {
            'Authorization': f'Bearer {self._api_key}',
            'accept': 'application/json'
        }
        response = await self.client.request(
            url=f"{self._end_point}{path}",
            method=method,
            params=params,
            data=data,
            headers=HEADERS,
            timeout=100000)
        json_response = response.json()
        if 'errors' in json_response:
            if isinstance(json_response['errors'], list):
                raise ApiError(f"Got err from host: {json_response['errors'][0]}")
            elif isinstance(json_response['errors'], dict):
                raise ApiError(f"Got err from host: {json_response['errors'].values()[0]}")
        return json_response

# 君の中にある　赤と青き線
# それらが結ばれるのは　心の臓
# 風の中でも負けないような声で
# 届ける言葉を今は育ててる
