# -*- coding: utf-8 -*-
from collections import Set
from urllib.parse import urljoin

import scrapy
from scrapy import Selector
from scrapy.http.response.html import HtmlResponse
from bs4 import BeautifulSoup


class GenericScraperSpider(scrapy.Spider):
    name = 'genericscraper'
    allowed_domains = []
    start_urls = []
    search_term = None
    visited_urls: set = {"#main"}

    def __init__(self, domains='', *args, **kwargs):
        super(GenericScraperSpider, self).__init__(*args, **kwargs)
        if domains:
            self.start_urls = domains.split(',')

        if kwargs['allowed_domains']:
            self.allowed_domains = kwargs['allowed_domains'].split(',')

        if kwargs['search_term']:
            self.search_term = kwargs['search_term']
        else:
            raise Exception("Please provide search term! Ex: "
                            "'scrapy.cmdline runspider generic_scraper.py "
                            "-a domain=https://thewirecutter.com -a search_term=refrigerator'")

    # request function
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        if response.meta['depth'] > 4:
            return
        self.visited_urls.add(response.url)
        hyperlinks = response.css('a::attr(href)').getall()
        h1_desc = response.css('h1::text').getall()
        p_desc = response.css('p::text').getall()
        div_desc = response.css('div::text').getall()
        a_desc = response.css('a::text').getall()
        unique_desc: set = set(p_desc)
        unique_desc.update(div_desc)
        unique_desc.update(h1_desc)
        # leave out hyperlinks for now since false positives.
        # unique_desc.update(a_desc)
        description_results = []
        for description in unique_desc:
            if self.search_term.lower() in description.lower():
                description_results.append(description)
        if description_results:
            yield {
                'url': response.url,
                'description': description_results,
                'search_term': self.search_term
            }

        junk_url_strings = ["@", "mail", "?merchant=", '?post=', ".jpg", ".mov", ".mp4", ".png", ".txt", ".mp3",
                            ".mpeg", "search"]
        for hyperlink in hyperlinks:
            junk_res = any(ele in hyperlink for ele in junk_url_strings)
            res = any(ele in hyperlink for ele in self.allowed_domains)
            if not junk_res:
                url = urljoin(response.url, hyperlink)
                if res and url not in self.visited_urls:
                    yield response.follow(hyperlink, callback=self.parse)
        # yield response.follow(author_url, callback=parse_author)
