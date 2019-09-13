from html.parser import HTMLParser

class ContentExtractionUtils:
    '''Some utility methods for parsing scraped content'''
    
    def extractLinks(self, content : str) -> list:
        ''' Extracts links from a content parameter '''
        return self.__extractLinksHtmlParser(content)

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
        if tag == "a":
            for name, value in attrs:
                if name == "href" and ContentExtractionUtils.validateLink(value) :
                    self.__links.append(value)

    def get_results(self):
        return self.__links