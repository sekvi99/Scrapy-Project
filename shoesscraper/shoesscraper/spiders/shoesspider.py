from typing import Any

import scrapy
from scrapy.http import Response

from shoesscraper.constans import BASE_URL, SPIDER_NAME
from shoesscraper.parsers.shoe_parser.shoe_parser import ShoeParser

from ..spiders.base_spider_class import BaseSpider


class ShoesSpider(BaseSpider):
    name = SPIDER_NAME
    start_urls = [BASE_URL]

    def __init__(self, *args, **kwargs):
        super(ShoesSpider, self).__init__(*args, **kwargs)
        self.collected_data = []

    def parse(self, response: Response) -> Any:
        # Instantiate your custom parser
        shoe_parser = ShoeParser(response)

        # Use the custom parser to get the parsed data
        collection_dto = shoe_parser.parse()

        # Append the parsed items to the collected data
        self.collected_data.extend([
            {
                'name': shoes_item.name,
                'price': shoes_item.price,
                'is_discounted': shoes_item.is_discounted,
                'is_new': shoes_item.is_new,
                'discount_percent': shoes_item.discount_percent
                # 'discount': shoes_item.discount,
                # 'is_new': shoes_item.is_new,
            }
            for shoes_item in collection_dto.collection
        ])
        
        print(self.collected_data)

        # Check if the "arrow-right" image is present
        arrow_right_img = response.css('img[src*="arrow-right_.svg"]')
        if arrow_right_img:
            self.log("Found 'arrow-right' image on page {}".format(response.url))

            # You can extract more data or perform actions before navigating to the next page

            # Extract the next page URL
            next_page_url = response.css('li.selected + li a::attr(href)').extract_first()
            if next_page_url:
                yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            self.log("No 'arrow-right' image found on page {}".format(response.url))

            # Yield the final result at the end
            print(self.collected_data)
            yield {
                'collection': self.collected_data,
                'count': len(self.collected_data),
            }
            
            