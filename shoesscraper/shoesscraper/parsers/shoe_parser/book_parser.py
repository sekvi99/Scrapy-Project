from dataclasses import dataclass
from typing import List, Union, Any

from ...consts.books_consts.constans import (
    PRODUCTS_LIST_SELECTOR, PRODUCT_RANK_SELECTOR, PRODUCT_NAME_SELECTOR, PRODUCT_AUTHOR_SELECTOR, PRODUCT_PRICE_SELECTOR,
    PRODUCT_PRICE_FROM_30_DAYS_SELECTOR, PRODUCT_PRICE_DISCOUNT_SELECTOR)
from ...items import BookItemDto
from ..abstract_parser import AbstractParser

@dataclass
class BookParser(AbstractParser):
    
    # * Section public methods
    def parse(self) -> List[BookItemDto]:
        items = []
        
        product_list = self.content.css(PRODUCTS_LIST_SELECTOR)
        for product in product_list:
            # Helpers
            is_price_before_thrity_days = self._is_price_before_thirty_days(product)
            
            # Object fields
            rank = self._extract_text(product, PRODUCT_RANK_SELECTOR)
            name = self._extract_text(product, PRODUCT_NAME_SELECTOR)
            author = self._extract_text(product, PRODUCT_AUTHOR_SELECTOR)
            price = self._get_price_value(self._extract_text(product, PRODUCT_PRICE_SELECTOR), ' ')
            price_before_thrity_days = self._get_price_value(self._extract_text(product, PRODUCT_PRICE_FROM_30_DAYS_SELECTOR), '\xa0') if is_price_before_thrity_days else None
            product_discount = self._get_product_discount(product)
            
            book_item = BookItemDto(
                product_rank=rank,
                name=name,
                author=author,
                price=price,
                price_before_thrity_days=price_before_thrity_days,
                product_discount=product_discount
            )
            items.append(book_item)
        return items
            
    # * Section private methods
    def _get_price_value(self, price_str: str, splitter: str) -> float:
        return float((price_str.split(splitter)[0]).replace(',', '.'))
    
    def _get_product_discount(self, product: Any) -> Union[str, None]:
        discount = self._extract_text(product, PRODUCT_PRICE_DISCOUNT_SELECTOR)
        return discount if discount else None
    
    def _is_price_before_thirty_days(self, product: Any) -> bool:
        return True if self._extract_text(product, PRODUCT_PRICE_FROM_30_DAYS_SELECTOR) else False