from typing import Final

# * Definition of spider shoes properties
BASE_URL: Final[str] = 'https://wojas.pl/buty-damskie'
SPIDER_NAME: Final[str] = 'shoes'

# Definition of page css selectors
PRODUCTS_LIST_SELECTOR: Final[str] = 'div.product-list__wrapper'
PRODUCT_NAME_SELECTOR: Final[str] = 'div.product-list__name h2::text'
PRODUCT_PRICE_SELECTOR: Final[str] = 'div.price-wrap div.product-list__price span::text'
PRODUCT_DISCOUNT_SELECTOR: Final[str] = 'div.product-list__tag div.other::text'
PRODUCT_DISCROUNTED_PRICE_SELECTOR: Final[str] = 'div.price-wrap div.box-list-product-price span::text'
PRODUCT_IS_NEW_SELECTOR: Final[str] = 'div.product-list__tag div.new::text'

# Definition of next page selector
PRODUCT_NEXT_PAGE_SELECTOR: Final[str] = 'img[src*="arrow-right_.svg"]'
NEXT_PAGE_URL_SELECTOR: Final[str] = 'li.selected + li a::attr(href)'