from simple_crawler_requests import SimpleCrawlerRequests
from simple_crawler_http import SimpleCrawlerHttp
from content_extraction_utils import ContentExtractionUtils

if __name__ == "__main__":
    crawlerReq = SimpleCrawlerRequests()
    url = input()
    print("fetching data from: " + url)
    output = open("content_crawled.log", "w")
    data = crawlerReq.crawl(url)
    output.write(data)
    #get all links in content
    tools = ContentExtractionUtils()
    links = tools.extractLinks(data)
    print(links)
    
    print("All done!")
    
