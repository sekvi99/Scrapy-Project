from typing import Any
import scrapy
from scrapy.http import Response
from shoesscraper.parsers.shoe_parser.shoe_parser import ShoeParser

class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    start_urls = ['https://wojas.pl/buty-damskie']
    
    def start_requests(self) -> None:
        for url in self.start_urls:
            yield scrapy.Request(url = url, callback=self.parse)
    
    def parse(self, response: Response) -> Any:
        # Instantiate your custom parser
        shoe_parser = ShoeParser(response)

        # Use the custom parser to get the parsed data
        collection_dto = shoe_parser.parse()

        # Yield the parsed items
        for shoes_item in collection_dto.items:
            yield {
                'name': shoes_item.name,
                'price': shoes_item.price,
                'discount': shoes_item.discount,
                'is_new': shoes_item.is_new,
            }

        # Check if the "arrow-right" image is present
        arrow_right_img = response.css('img[src*="arrow-right_.svg"]')
        print(arrow_right_img)
        if arrow_right_img:
            self.log("Found 'arrow-right' image on page {}".format(response.url))

            # You can extract more data or perform actions before navigating to the next page

            # Extract the next page URL
            next_page_url = response.css('li.selected + li a::attr(href)').extract_first()
            if next_page_url:
                yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            self.log("No 'arrow-right' image found on page {}".format(response.url))
            
            