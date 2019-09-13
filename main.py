from simple_crawler_requests import SimpleCrawlerRequests
from simple_crawler_http import SimpleCrawlerHttp
from content_extraction_utils import ContentExtractionUtils

if __name__ == "__main__":
    crawlerReq = SimpleCrawlerRequests()
    url = input("Crawl address for single crawl: ")
    print("fetching data from: " + url)
    output = open("content_crawled.log", "w")
    data = crawlerReq.crawl(url)
    output.write(data)
    #get all links in content
    tools = ContentExtractionUtils()
    links = tools.extractLinks(data)
    print("found " + str(len(links)) + " links in " + url)

    url = input("Crawl address for multiple levels: ")
    levels = int(input("Levels for crawl depth: "))
    result = crawlerReq.crawlMultipleLevels(url, levels)
    print("fetching data for " + url)
    print("found " + str(len(result)) + " links in " + url + " with " + str(levels) + " depth levels")

    print("All done!")
    
