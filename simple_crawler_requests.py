import requests

class SimpleCrawlerRequests :
    ''' a simple crawler that uses the requests package '''

    def __init__(self):

    def crawl(self, url, parameters=None):
        response = requests.get(url)
        return response.text