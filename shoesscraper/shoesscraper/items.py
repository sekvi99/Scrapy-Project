from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel

# * Definition of generic type for all of the spider response models
TDataType = TypeVar('TDataType')

class ShoesItemDto(BaseModel):
    name: str # Shoe name
    price: float # Shoe price
    is_discounted: Optional[bool] # Is shoe in discount
    is_new: Optional[bool] # Is new kind of shoe
    discount_percent: Optional[int] # Per cent of discount

class BookItemDto(BaseModel):
    product_rank: str # Order in bestsellers
    name: str # Book name
    author: Optional[str] # Author name
    price: float # Book price
    price_before_thrity_days: Optional[float] # Book price from 30 days
    product_discount: Optional[str] # Book discount

class ScrapCollectionDto(BaseModel, Generic[TDataType]):
    collection: List[TDataType] # Collection of scrapped items
    count: int # Amount of those items
