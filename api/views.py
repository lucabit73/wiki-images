from django.http import JsonResponse
from api.wikipedia_client import WikipediaClient
from requests.exceptions import RequestException

def index(request):
    cli = WikipediaClient()
    try:
        resp = cli.getSomething()
    except RequestException as e:
        return JsonResponse({"Error with Wikipedia API": "{}".format(e)})
    return JsonResponse(resp)
