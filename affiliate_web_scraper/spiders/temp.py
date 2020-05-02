# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.http.response.html import HtmlResponse
from bs4 import BeautifulSoup


class TheWireCutterSpider(scrapy.Spider):
    name = 'thewirecutter'
    allowed_domains = ['thewirecutter']
    start_urls = ['https://thewirecutter.com/reviews/the-best-refrigerator/']

    def __init__(self, domain='', *args, **kwargs):
        super(TheWireCutterSpider, self).__init__(*args, **kwargs)
        if domain:
            self.start_urls = [domain]

    # request function
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # self.logger.info('hello this is my first spider')
        posts = response.css('div.ba62891a')
        sections = response.css('section.c13297ef')
        item_boxes = response.xpath('//div[@data-scp="callout"]')
        hyperlinks = response.css('a::attr(href)').getall()
        for item_ in item_boxes:
            test_item = item_.xpath('./div[@data-scp="callout_item"]')
            for div_box in test_item:
                image_url = div_box.xpath('./div/div/div[1]/a/figure/img/@data-src').extract_first()

                item_title = div_box.xpath('./div/div/div[2]/*[1]/a/text()').extract_first()
                bullet_points = div_box.xpath('./div/div/div[2]/*[2]/a/text()').extract_first()
                description = div_box.xpath('./div/div/div[2]/*[3]/text()').extract_first()
                yield {
                    'image_url': image_url,
                    'title': item_title,
                    'bullet_points': bullet_points,
                    'description': description,
                }

        #
        # xpath = response.xpath('//section[@class="c13297ef"]/p/*').extract()
        # test = response.xpath('//section/following-sibling::div').extract()
        # test2 = response.xpath('//section[p]').extract()
        # for section in sections:
        #     text_test = section.xpath('./p/text()').extract()
        #     xpath = section.xpath('.//div[@class="c35e99f0"]')
        #     link = section.xpath('./p/a/@href').extract()
        #     print(f"{text_test}:  {link}")
        # for post in posts:
        #     title = post.css('h3.aead67f5 ::text').get()
        #     title_link = post.css('h3.aead67f5 a::attr(href)').get()
        #     text = post.css('p._84165eda ::text').getall()
        #     description = ''.join(text).strip()
        #     links = post.css('div.c-product-widget__content a::attr(href)').getall()
        #     yield {
        #         'title': title,
        #         'description': description,
        #         'links': title_link,
        #
        #     }


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
