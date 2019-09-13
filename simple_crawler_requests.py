from crawler import Crawler
from content_extraction_utils import ContentExtractionUtils
import requests
import time

class SimpleCrawlerRequests(Crawler) :
    ''' a simple crawler that uses the requests package '''
    MAX_LEVELS = 5

    def __init__(self):
        super().__init__()

    def crawl(self, url, params=None):
        try:
            response = requests.get(url, params)
            return response.text
        except requests.exceptions.SSLError:
            print("ssl error for " + url)
        return None

    def crawlMultipleLevels(self, url, levels=1, params=None):
        if levels > self.MAX_LEVELS:
            print("Too many levels for crawling")
            return {}
        
        tools = ContentExtractionUtils()
        results = {}
        linksForNextLevel = []
        while levels > 0:
            print("getting links for level " + str(levels))
            if len(linksForNextLevel) == 0:
                print("requesting " + url)
                content = self.crawl(url, params)
                results[url] = content
                linksForNextLevel = tools.extractLinks(content)
            else:
                tempLinks = []
                for link in linksForNextLevel:
                    #don't add duplicates
                    if link not in results:
                        print("requesting " + link)
                        content = self.crawl(link, params)
                        time.sleep(1) #avoid too many too fast requests
                        if content is not None:
                            results[link] = content
                            tempLinks += list(set(tools.extractLinks(content)))
                linksForNextLevel = tempLinks

            levels = levels - 1
        
        return results