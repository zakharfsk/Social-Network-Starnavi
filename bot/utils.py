import requests

BASE_URL = 'http://127.0.0.1:8000/api'


def make_request(method: str, url: str, data: dict = None, headers: dict = None):
    """
    Sends an HTTP request to the specified URL using the specified method.

    Args:
        method (str): The HTTP method to use for the request (e.g. 'GET', 'POST', etc.).
        url (str): The URL to send the request to.
        data (dict, optional): The data to include in the request body (if applicable).
        headers (dict, optional): The headers to include in the request.

    Returns:
        The response object returned by the server.
    """
    return requests.request(
        method,
        url,
        data=data,
        headers=headers
    )
