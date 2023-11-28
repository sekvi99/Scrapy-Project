import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

import scrapy

from shoesscraper.consts.env_consts import SAVE_RESULTS_DIR
from shoesscraper.items import ScrapCollectionDto, TDataType


@dataclass
class BaseSpider(scrapy.Spider):
    
    _collected_items: List[TDataType] = field(default_factory=list)
    _output_dir: str = field(default=SAVE_RESULTS_DIR)
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def start_requests(self) -> None:
        for url in self.start_urls:
            yield scrapy.Request(url = url, callback=self.parse)
            
    def save_response(self) -> None:
        # Creating collection to save
        colection_dto = ScrapCollectionDto(collection=self._collected_items, count=len(self._collected_items))
        collection_dict = colection_dto.dict()
        
        # Setting up dir and file
        output_dir = Path(self._output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f'{self.name}_collection.json'
        
        # Saving output
        with output_file.open(mode='w') as f:
            json.dump(collection_dict, f, indent=2)
        
    def closed(self, reason: str) -> None:
        # Calling save after spider is closed
        self.save_response()