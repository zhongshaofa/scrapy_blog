# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBlogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 标题
    title = scrapy.Field()
    # 描述
    describe = scrapy.Field()
    # 创建时间
    create_at = scrapy.Field()
    # 作者
    auther = scrapy.Field()
    # 点击量
    clicks = scrapy.Field()
    # 点赞量
    praise = scrapy.Field()

    pass
