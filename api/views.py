from django.http import JsonResponse
from api.wikipedia_client import WikipediaClient
from requests.exceptions import RequestException
from .wikipedia_client import DecodingException


def index(request):
    cli = WikipediaClient()
    status_code = 200
    try:
        # resp = cli.get_page_from_title('it', 'Mercurio')
        # resp = cli.get_page_from_title('it', 'Cane mangia cane (film)')
        # resp = cli.get_pages_from_title('it', 'cane', 10)
        resp = cli.get_page('it', 2438904)
    except (RequestException, DecodingException):
        resp = {"error": "An error occurred while retrieving Wikipedia data"}
        status_code = 500

    return JsonResponse(data=resp, status=status_code)
