from dataclasses import dataclass
import scrapy
from typing import List, Generic, TypeVar, Optional

# * Definition of generic type for all of the spider response models
TDataType = TypeVar('TDataType')

@dataclass(frozen=True)
class ShoesItemDto(scrapy.Item):
    name: str # Shoe name
    price: float # Shoe price
    is_discounted: Optional[bool] # Is shoe in discount
    # is_new: Optional[bool] # Is new kind of shoe
    discount_percent: Optional[float] # Per cent of discount


class ScrapCollectionDto(scrapy.Item, Generic[TDataType]):
    collection: List[TDataType] # Collection of scrapped items
    count: int # Amount of those items
