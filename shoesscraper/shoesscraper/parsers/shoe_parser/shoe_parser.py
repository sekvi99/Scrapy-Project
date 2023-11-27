from ..abstract_parser import AbstractParser
from dataclasses import dataclass
from scrapy.http import Response
from ...items import ScrapCollectionDto, ShoesItemDto
from ...constans import PRODUCTS_LIST_SELECTOR, PRODUCT_NAME_SELECTOR, PRODUCT_PRICE_SELECTOR, PRODUCT_DISCOUNT_SELECTOR, PRODUCT_IS_NEW_SELECTOR
from typing import Union
@dataclass
class ShoeParser(AbstractParser):
    """_summary_

    Args:
        AbstractParser (_type_): _description_

    Returns:
        _type_: _description_
    """
    # * Section public methods
    def parse(self) -> ScrapCollectionDto[ShoesItemDto]:
        items = []
        
        product_list = self.content.css(PRODUCTS_LIST_SELECTOR)
        for product in product_list:
            name = self._extract_text(product, PRODUCT_NAME_SELECTOR)
            price = self._extract_text(product, PRODUCT_PRICE_SELECTOR)
            discount_percent = self._extract_text(product, PRODUCT_DISCOUNT_SELECTOR)
            is_new = self._extract_text(product, PRODUCT_IS_NEW_SELECTOR)
            print(name, price, discount_percent, is_new)
            print(ShoesItemDto(
                name=name,
                price=price,
                discount_percent=discount_percent,
                is_new=is_new
            ))
            shoes_item = ShoesItemDto(name=name, price=price, discount_percent=discount_percent, is_new=True if is_new else None)
            items.append(shoes_item)
        return ScrapCollectionDto(items=items, count=len(items))
        
    # * Section private methods
    def _extract_text(self, element: Response.body, selector: str) -> Union[str, None]:
        selected_element = element.css(selector).get()
        return selected_element.strip() if selected_element else None
