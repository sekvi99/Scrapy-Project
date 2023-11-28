# Scrapy Project
To run and play with existing project you're suppose to have already installed python at your PC.

# Project Structure
The project created contains further folders:
* **consts** - Constants needed for the spider in question,
* **page_handlers** - Parsers needed to extract the url of the next subpage,
* **parsers** - Parsers needed to export information from the response object,
* **results** - Examples of spider results,
* **spiders** - Definition of spiders.

# Project Set up
To proppery run project, u need to install requirements specified in file _requirements.txt_.\
To achive this step type.
```
pip install -r requirements.txt
```
In terminal of your preference.

# Run Scrapy shell
To spectate web page content, run those commands.
```
scrapy shell # Opens scrapy shell in terminal
fetch('{url}') # Fetch content of provided url
response... # Modify and play with response object as you like
```

# Run existing spiders
Running existing spiders with commends provided below, will create result files in dir: results.
```
scrapy crawl shoes # shoes_collection.json
scrapy crawl books # books_collection.json
```

# Run base tests
Test check only whether whole process of crawling does not effect any errors.\
From main directory run below.
```
pytest shoesscraper/tests/test_book_spider.py
pytest shoesscraper/tests/test_shoes_spider.py
```