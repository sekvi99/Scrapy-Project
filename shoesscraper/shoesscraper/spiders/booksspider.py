from typing import Any

import scrapy
from scrapy.http import Response

from shoesscraper.consts.books_consts.constans import (
    BASE_URL, CUT_OFF_BASE_URL, NEXT_PAGE_URL_SELECTOR,
    PRODUCT_NEXT_PAGE_SELECTOR, SPIDER_NAME)
from shoesscraper.page_handlers.handers.books_page_handler import \
    BooksNextPageHandler
from shoesscraper.parsers.parsers.book_parser import BookParser

from ..spiders.base_spider_class import BaseSpider


class BooksSpider(BaseSpider):
    name = SPIDER_NAME
    start_urls = [BASE_URL]

    def parse(self, response: Response) -> Any:
        # Parsing page content
        shoe_parser = BookParser(response)
        parsed_items = shoe_parser.parse()
        self._collected_items.append(parsed_items)
        
        # Skipping to next page
        next_page_handler = BooksNextPageHandler(response, PRODUCT_NEXT_PAGE_SELECTOR, NEXT_PAGE_URL_SELECTOR)
        if next_page_handler.has_next_page():
            next_page_url = next_page_handler.extract_next_page_url()
            if next_page_url:
                yield scrapy.Request(url=f'{CUT_OFF_BASE_URL}{next_page_url}', callback=self.parse)