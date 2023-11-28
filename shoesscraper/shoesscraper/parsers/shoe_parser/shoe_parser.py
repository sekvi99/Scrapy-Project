from dataclasses import dataclass
from typing import List, Union

from scrapy.http import Response

from ...consts.shoes_consts.constans import (
    PRODUCT_DISCROUNTED_PRICE_SELECTOR, PRODUCT_IS_NEW_SELECTOR,
    PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR, PRODUCTS_LIST_SELECTOR)
from ...items import ShoesItemDto
from ..abstract_parser import AbstractParser


@dataclass
class ShoeParser(AbstractParser):

    # * Section public methods
    def parse(self) -> List[ShoesItemDto]:
        items = []
        
        product_list = self.content.css(PRODUCTS_LIST_SELECTOR)
        for product in product_list:
            
            # Helpers
            price_str = self._extract_text(product, PRODUCT_PRICE_SELECTOR)
            is_product_discounted = self._is_price_discounted(price_str)
            product_price_after_discount = self._extract_text(product, PRODUCT_DISCROUNTED_PRICE_SELECTOR) if is_product_discounted else None
            
            # Object fields
            name = self._extract_text(product, PRODUCT_NAME_SELECTOR)
            price = self._get_price_value(product_price_after_discount) if is_product_discounted else self._get_price_value(price_str)
            discount_percent = self._get_discount_percent(price_str) if is_product_discounted else None
            is_new = self._is_new_product(self._extract_text(product, PRODUCT_IS_NEW_SELECTOR))
            shoes_item = ShoesItemDto(
                name=name,
                price=price,
                is_discounted=is_product_discounted,
                is_new=is_new,
                discount_percent=discount_percent
                )
            items.append(shoes_item)
        return items
        
    # * Section private methods
    def _extract_text(self, element: Response.body, selector: str) -> Union[str, None]:
        selected_element = element.css(selector).get()
        return selected_element.strip() if selected_element else None

    def _is_price_discounted(self, price_str: str) -> bool:
        return True if '%' in price_str else False
    
    def _is_new_product(self, new_str: str | None) -> bool:
        return True if new_str != None else False
    
    def _get_price_value(self, price_str: str) -> float:
        return float(price_str.split('.')[0])
    
    def _get_discount_percent(self, discount_str) -> int:
        return int(''.join(filter(str.isdigit, discount_str)))
