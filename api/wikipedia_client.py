from django.conf import settings
import requests
from requests.exceptions import RequestException
import logging


class DecodingException(Exception):
    pass


class WikipediaClient(object):
    def __init__(self):
        self.url = settings.WIKIPEDIA_API
        self.query_params = {
            'action': 'query',
            'format': 'json',
            'formatversion': 2,
        }

    def wiki_request(self, params, lang):
        url = self.url.format(lang=lang)

        try:
            response = requests.get(url, params)
            response.raise_for_status()
        except RequestException as e:
            logging.error("RequestException: {}".format(e))
            raise

        try:
            result = response.json()
        except Exception as e:
            logging.error("Exception while decoding response json: {}".format(e))
            raise DecodingException("{}".format(e))
        return result

    def get_something(self):
        params = self.query_params.copy()
        params.update({'prop': 'pageprops', 'titles': "casa"})
        response = self.wiki_request(params, 'it')
        return response



