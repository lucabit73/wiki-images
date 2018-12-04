from django.conf import settings
import requests
from requests.exceptions import RequestException
import logging


class DecodingException(Exception):
    pass


class Page(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title
        # self.disambiguation Bool
        # self.page_image_free Str

    def __str__(self):
        return self.title

    @classmethod
    def from_page_response_item(cls, obj):
        return cls(obj['pageid'], obj['title'])


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

    def get_page_from_title(self, lang, title):
        params = self.query_params.copy()
        params.update({'prop': 'pageprops', 'titles': title})
        response = self.wiki_request(params, lang)
        return response

    def get_page(self, lang, id):
        # https://www.mediawiki.org/wiki/API:Query
        params = self.query_params.copy()
        params.update({'prop': 'pageprops', 'pageids': id})
        response = self.wiki_request(params, lang)

        # Try to build a Page object
        # is useful?
        page_item = response['query']['pages'][0]
        page_obj = Page.from_page_response_item(page_item)
        logging.warning(page_obj)

        return response

    def get_pages_from_title(self, lang, title, count):
        # https://www.mediawiki.org/wiki/API:Search
        params = self.query_params.copy()
        params.update({
            'prop': 'pageprops',
            'list': 'search',
            'srlimit': count,
            'srsearch': title,
            'srprop': ''})
        response = self.wiki_request(params, lang)
        return response


