from scrapy.http import Response


class StaticParser:
    
    @staticmethod
    def parse(response: Response, selector: str) -> bool:
        return True if response.css(selector) else False