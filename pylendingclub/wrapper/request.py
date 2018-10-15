import requests

class Request():
    """
    Base class for sending a GET or POST request.
    """
    def send(self, query_params=None, payload=None):
        """
        Creates and sends the request.

        This method should be accessed only through a derived Request class where the
        method has been overridden with the implementation logic.
        """
        raise NotImplementedError('Send method accessed from base class. Should be accessed from derived' +
                                  ' GetRequest or PostRequest')

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

class GetRequest(Request):
    """
    Sends GET requests.
    """
    def send(self, query_params=None):
        return requests.get(url=self._url, params=query_params, headers=self._headers)

class PostRequest(Request):
    """
    Sends POST requests.
    """
    def send(self, payload=None):
        return requests.post(self._url, json=payload, headers=self._headers)
