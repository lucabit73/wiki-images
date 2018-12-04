from django.conf import settings
import requests
from requests import ConnectionError, HTTPError, Timeout
import logging


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
        except ConnectionError as e:
            logging.error("ConnectionError: {}".format(e))
            raise
        except HTTPError as e:
            logging.error("HTTPError: {}".format(e))
            raise
        except Timeout as e:
            logging.error("Timeout: {}".format(e))
            raise
        try:
            result = response.json()
        except Exception as e:
            logging.error("Exception while decoding response json: {}".format(e))
            raise
        return result

    def get_something(self):
        params = self.query_params.copy()
        params.update({'prop': 'pageprops', 'titles': "casa"})
        response = self.wiki_request(params, 'it')
        return response



