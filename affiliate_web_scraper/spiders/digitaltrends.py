# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse


class DigitalTrendsSpider(scrapy.Spider):
    name = 'digitaltrends'
    allowed_domains = ['digitaltrends']
    start_urls = ['https://www.digitaltrends.com/appliance-reviews/']

    # request function
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # self.logger.info('hello this is my first spider')
        posts = response.css('div.b-brief')
        for post in posts:
            testing = post.css('.a').get()
            test = post.css('.div.h3.a').get()
            yield {
                'text': post.css('.div.h2::a').get(),

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
