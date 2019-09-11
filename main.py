from simple_crawler_requests import SimpleCrawlerRequests
from simple_crawler_http import SimpleCrawlerHttp
from content_extraction_utils import ContentExtractionUtils, ParsingType

if __name__ == "__main__":
    crawlerReq = SimpleCrawlerRequests()
    url = input()
    print("fetching data from: " + url)
    output = open("content_crawled.log", "w")
    data = crawlerReq.crawl(url)
    output.write(data)
    #get all links in content
    tools = ContentExtractionUtils()
    links = tools.extractLinks(data, ParsingType.MANUAL)
    print(len(links))
    links = tools.extractLinks(data, ParsingType.HTMLPARSER)
    print(len(links))
    
    print("All done!")
    
