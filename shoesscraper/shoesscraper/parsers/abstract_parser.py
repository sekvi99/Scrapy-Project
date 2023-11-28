from abc import ABC, abstractmethod
from dataclasses import dataclass

from scrapy.http import Response

from ..items import ScrapCollectionDto, TDataType


@dataclass
class AbstractParser(ABC):
    
    content: Response # Scrapy response object
    
    @abstractmethod
    def parse(self) -> ScrapCollectionDto[TDataType]:
        """
        Should parse content from response to provided TDataType of ScrapCollectionDto.
        """
        ...
