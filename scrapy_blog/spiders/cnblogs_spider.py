# -*- coding: utf-8 -*-
import scrapy
from scrapy_blog.items import ScrapyBlogItem


class CnblogsSpiderSpider(scrapy.Spider):
    name = 'cnblogs_spider'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']

    def parse(self, response):
        list = response.xpath("//div[@id='post_list']//div[@class='post_item']")
        print(list)
        pass
