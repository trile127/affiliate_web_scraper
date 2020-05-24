# Generic Web Scraper for Affiliate Website Products

# Installation
Requires Python 3.6.5 and up
```shell script
pip install -r requirements.txt
```

## Parameters:
```bash
-o <name_of_file> Output file to write to. EX: url_results.json. Will write it to <path-to>/affiliate_web_scraper/affiliate_web_scraper/spiders/<name_of_file>

-a domains=<domains> Scrapes specific list of domains, delimited by ',' (comma)
-a allowed_domains=<allowed_domains> Does not scrape any url that is outside these allowed domains, delimited by ','
-a search_term=<exact phrase to find> Checks text descriptions of html page for this term
```

# Run from Pycharm:
```bash
# Tested on Windows
scrapy.cmdline runspider generic_scraper.py -o url_results.json -a domains=https://thewirecutter.com/,https://appliancebuyersguide.com -a allowed_domains=thewirecutter.com,appliancebuyersguide.com -a search_term=SHEM63W55N
```


# Run from Command Line:
```bash
# From directory: <path-to>/affiliate_web_scraper/
scrapy runspider affiliate_web_scraper/spiders/generic_scraper.py -o url_results.json -a domains=https://thewirecutter.com/,https://appliancebuyersguide.com -a allowed_domains=thewirecutter.com,appliancebuyersguide.com -a search_term=SHEM63W55N
```

# Notes
Do not use on digitaltrends.com or consumeraffairs.com