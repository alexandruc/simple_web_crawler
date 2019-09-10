from crawler import Crawler
import requests

class SimpleCrawlerRequests(Crawler) :
    ''' a simple crawler that uses the requests package '''

    def __init__(self):
        super().__init__()

    def crawl(self, url, parameters=None):
        response = requests.get(url)
        return response.text