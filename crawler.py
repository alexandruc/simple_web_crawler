from abc import ABC, abstractmethod

class Crawler:
    def __init__(self):
        self.url = ""
        self.params = {}

    @abstractmethod
    def crawl(self, url, params = None):
        pass