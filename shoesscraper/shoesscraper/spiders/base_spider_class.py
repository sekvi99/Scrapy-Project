import scrapy


class BaseSpider(scrapy.Spider):
    
    def start_requests(self) -> None:
        for url in self.start_urls:
            yield scrapy.Request(url = url, callback=self.parse)