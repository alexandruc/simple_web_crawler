from enum import Enum, unique
from html.parser import HTMLParser

@unique
class ParsingType(Enum):
    MANUAL = 1
    HTMLPARSER = 2

class ContentExtractionUtils:
    '''Some utility methods for parsing scraped content'''
    
    def extractLinks(self, content : str, method = ParsingType.HTMLPARSER) -> list:
        ''' Extracts links from a content parameter '''
        if method == ParsingType.MANUAL:
           return self.__extractLinksManual(content)
        elif method == ParsingType.HTMLPARSER:
            return self.__extractLinksHtmlParser(content)
        return []

    def __extractLinksManual(self, content):
        start = 0
        links = []
        linkStartPattern = "href=\""
        while start != -1:
            start = content.find(linkStartPattern ,start)
            if start != -1:
                start += len(linkStartPattern)
                end = content.find("\"", start+len(linkStartPattern))
                if end != -1:
                    data = content[start : end]
                    if ContentExtractionUtils.validateLink(data):
                        links.append(data)
                    start = end+1
        return links

    def __extractLinksHtmlParser(self, content):
        html_parser = LinkExtractor()
        html_parser.feed(content)
        return html_parser.get_results()

    @staticmethod
    def validateLink(link : str):
        ''' poor man's check if link is valid http link '''
        return link.startswith("http")

class LinkExtractor(HTMLParser):
    __links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == "href" and ContentExtractionUtils.validateLink(value) :
                self.__links.append(value)

    def get_results(self):
        return self.__links