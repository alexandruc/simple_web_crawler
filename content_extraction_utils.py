
class ContentExtractionUtils:
    '''Some utility methods for parsing scraped content'''
    
    def extractLinks(self, content : str) -> list:
        ''' Extracts links from a content parameter '''
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
                    if self.__validateLink(data):
                        links.append(data)
                    start = end+1
        return links

    def __validateLink(self, link : str):
        ''' poor man's check if link is valid http link '''
        return link.startswith("http")

