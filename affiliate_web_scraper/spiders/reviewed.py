# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.http.response.html import HtmlResponse


class ReviewedSpider(scrapy.Spider):
    name = 'reviewed'
    allowed_domains = ['reviewed']
    start_urls = ['https://www.reviewed.com/dishwashers/best-right-now/best-dishwashers']

    # request function
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # self.logger.info('hello this is my first spider')
        posts = response.css('div.c-product-widget')
        for post in posts:
            title = post.css('div.u2::text').get()
            text = post.css('div.c-product-widget__content ::text').getall()
            description = ''.join(text).strip()
            links = post.css('div.c-product-widget__content a::attr(href)').getall()
            yield {
                'title': title,
                'description': description,
                'links': links,

            }




    #         author_url = quote.css('.author + a::attr(href)').get()
    #         self.logger.info('get author page url')
    #         # go to the author page
    #         url = response.urljoin(author_url)
    #         yield response.follow(author_url, callback=self.parse_author)
    #         # yield response.follow(author_url, callback=parse_author)
    #
    #     for a in response.css('li.next a'):
    #         yield response.follow(a, callback=self.parse)
    #
    # def parse_author(self, response):
    #     self.logger.info('parse_author')
    #     yield {
    #         'author_name': response.css('.author-title::text').get(),
    #         'author_birthday': response.css('.author-born-date::text').get(),
    #         'author_bornlocation': response.css('.author-born-location::text').get(),
    #         'author_bio': response.css('.author-description::text').get(),
    #     }
