from simple_crawler_requests import SimpleCrawlerRequests

if __name__ == "__main__":
    crawlerReq = SimpleCrawlerRequests()
    print(crawlerReq.crawl("http://httpbin.org/get"))
