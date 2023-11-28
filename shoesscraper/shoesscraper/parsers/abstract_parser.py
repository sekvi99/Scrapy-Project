from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Union

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
        
    def _extract_text(self, element: Response.body, selector: str) -> Union[str, None]:
        selected_element = element.css(selector).get()
        return selected_element.strip() if selected_element else None
