from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from scrapy.http import Response

from ..items import TDataType


@dataclass
class AbstractParser(ABC):
    
    content: Response # Scrapy response object
    
    @abstractmethod
    def parse(self) -> List[TDataType]:
        """
        Should parse content from response to provided TDataType of ScrapCollectionDto.
        """
        ...
