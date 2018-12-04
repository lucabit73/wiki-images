from django.http import JsonResponse
from api.wikipedia_client import WikipediaClient
from requests.exceptions import RequestException
from .wikipedia_client import DecodingException


def index(request):
    cli = WikipediaClient()
    status_code = 200
    try:
        resp = cli.get_something()
    except (RequestException, DecodingException):
        resp = {"error": "An error occurred while retrieving Wikipedia data"}
        status_code = 500

    return JsonResponse(data=resp, status=status_code)
