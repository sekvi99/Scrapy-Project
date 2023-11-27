from dataclasses import dataclass
from scrapy.http import Response
from abc import ABC, abstractmethod
from ..items import ScrapCollectionDto, TDataType

@dataclass
class AbstractParser(ABC):
    
    content: Response
    
    @abstractmethod
    def parse(self) -> ScrapCollectionDto[TDataType]:
        ...
