from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from scrapy.http import Response

from ..parsers.static_parser import StaticParser


@dataclass
class AbstractNextPageHandler(ABC):
    
    response: Response
    next_page_selector: str
    next_page_url_selector: str
    
    @abstractmethod
    def has_next_page(self) -> bool:
        """
        Should check whether next page is accesiblle
        """
        ...
        
    @abstractmethod
    def extract_next_page_url(self) -> Optional[str]:
        """
        Should extract next page url
        """
        ...
        
@dataclass
class BaseNextPageHandler(AbstractNextPageHandler):
    
    def has_next_page(self) -> bool:
        return StaticParser.parse(self.response, self.next_page_selector)
    
    def extract_next_page_url(self) -> Optional[str]:
        return self.response.css(self.next_page_url_selector).extract_first()