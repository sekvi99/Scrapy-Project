from scrapy.crawler import CrawlerRunner
from shoesscraper.spiders.booksspider import BooksSpider
from twisted.internet import reactor
import pytest

def test_spider_run_without_errors():
    # Create a test runner and run the spider
    runner = CrawlerRunner()
    deferred = runner.crawl(BooksSpider)
    deferred.addBoth(lambda _: reactor.stop())
    reactor.run()

    # Check if the spider completed without errors
    assert deferred.result is None
