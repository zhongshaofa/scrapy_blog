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
    # 文章封面
    cover_img = scrapy.Field()
    # 描述
    describe = scrapy.Field()
    # 详细链接
    url = scrapy.Field()
    # 文章内容
    content = scrapy.Field()
    # 创建时间
    create_time = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 作者头像
    head_img = scrapy.Field()
    # 点击量
    clicks = scrapy.Field()
    # 点赞量
    praise = scrapy.Field()
    # 头像下载后的路径
    head_img_paths = scrapy.Field()
    # 文章图片原本路径
    article_img_list = scrapy.Field()
    # 文章图片下载后的路径
    article_img_paths = scrapy.Field()

    pass
