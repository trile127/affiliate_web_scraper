#!/bin/bash
NOW=$(date +"%m-%d-%Y")
SEARCH_TERM="SHEM63W55N"
FILE_NAME="$SEARCH_TERM-$NOW-results.json"
DOMAINS="https://thewirecutter.com/,https://appliancebuyersguide.com"
ALLOWED_DOMAINS="thewirecutter.com,appliancebuyersguide.com"
scrapy runspider affiliate_web_scraper/spiders/generic_scraper.py -o FILE_NAME -a domains=$DOMAINS -a allowed_domains=$ALLOWED_DOMAINS -a search_term=$SEARCH_TERM