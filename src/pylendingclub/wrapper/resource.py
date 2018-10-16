from pylendingclub.wrapper.base import Base
from pylendingclub.wrapper.request import GetRequest, PostRequest


class Resource(Base):
    """
    Base class for all resources within the API.
    """
    def _get_request(self, sub_url):
        """
        Constructor for a new GetRequest.

        Handles constructing the URL for the request, as well as providing the headers.
        Using the default constructor by creating a new class will not cause issues, as long as the
        headers, and url, are properly provided.
        """
        return GetRequest(self.join_url(self._url, sub_url), self._headers)


    def _post_request(self, sub_url):
        """
        Constructor for a new PostRequest.

        Handles constructing the URL for the request, as well as providing the headers.
        Using the default constructor by creating a new class will not cause issues, as long as the
        headers, and url, are properly provided.
        """
        return PostRequest(self.join_url(self._url, sub_url), self._headers)


    def __init__(self, url, headers):
        self._url = url
        self._headers = headers
