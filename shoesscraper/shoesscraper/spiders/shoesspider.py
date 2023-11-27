from typing import Any
import scrapy
from scrapy.http import Response
import base64

class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    start_urls = ['https://wojas.pl/buty-damskie']
    
    def parse(self, response: Response) -> Any:
        for products in  response.css('div.product-list__wrapper') :
            yield {
                'name': products.css('div.product-list__name h2::text').get() ,
                'price': products.css('div.price-wrap div.product-list__price span::text').get(),
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
            
            