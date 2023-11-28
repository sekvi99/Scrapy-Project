from typing import Final

# * Definition of spider phones properites
BASE_URL: Final[str] = 'https://www.taniaksiazka.pl/bestsellery'
CUT_OFF_BASE_URL: Final[str] = 'https://www.taniaksiazka.pl'
SPIDER_NAME: Final[str] = 'books'

# Definition of page css selectors
PRODUCTS_LIST_SELECTOR: Final[str] = 'div.product-container'
PRODUCT_RANK_SELECTOR: Final[str] = 'div.top-label-container div.top-label::text'
PRODUCT_NAME_SELECTOR: Final[str] = 'h2 a.ecommerce-datalayer::text'
PRODUCT_AUTHOR_SELECTOR: Final[str] = 'div.product-authors a::text'
PRODUCT_PRICE_SELECTOR: Final[str] = 'div.product-main-bottom span.updateable span.product-price::text'
PRODUCT_PRICE_FROM_30_DAYS_SELECTOR: Final[str] = 'div.product-main-bottom span.updateable span.p-lowest-price span.p-lowest-price-values span.p-lowest-price-amount::text'
PRODUCT_PRICE_DISCOUNT_SELECTOR: Final[str] = 'div.product-main-bottom span.updateable span.p-lowest-price span.p-lowest-price-values span.p-percent-discount::text'

# Definition of next page selector
PRODUCT_NEXT_PAGE_SELECTOR: Final[str] = 'div.page-index li.next'
NEXT_PAGE_URL_SELECTOR: Final[str] = 'div.page-index li.next a::attr(href)'