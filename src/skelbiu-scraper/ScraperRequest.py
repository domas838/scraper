import string

from config import config
import requests


class ScraperRequest:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': config.USER_AGENT['user_agent']}

    def request(self) -> requests:
        return requests.get(self.url, headers=self.headers)
