# -*- coding: utf-8 -*-
import pymysql
import json
import codecs
from scrapy import Request
from scrapy_blog.settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DBNAME
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy_blog import log


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyBlogPipeline(object):

    # 初始化mysql服务
    def __init__(self):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DBNAME)
        self.cursor = self.db.cursor()

    # 持久化数据到数据库中
    def process_item(self, item, spider):

        # 查询数据库中是否存在该数据
        query = "SELECT * from article WHERE title='" + item['title'] + "'"
        self.cursor.execute(query)
        article = self.cursor.fetchall()
        if article:
            return "数据库中已存在该文章:" + item['title']

        item['content'] = self.correct_content(item['content'], item['article_img_list'], item['article_img_paths'])

        # 插入数据库中去
        insert = "INSERT INTO article " \
                 "(`author`, `clicks`, `content`,  `create_time`, `describe`, `head_img`, `praise`, `title`, `url`)\
        VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                 % (item['author'], item['clicks'], pymysql.escape_string(item['content']), item['create_time'],
                    item['describe'], item['head_img'],
                    item['praise'], item['title'], item['url'])
        try:
            self.cursor.execute(insert)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return e
        log.msg(item['title'], '插入成功')
        return item['title']

    # 替换文章图片
    def correct_content(self, content, article_img_list, article_img_paths):
        log.msg(article_img_list,'下载前文章图片')
        log.msg(article_img_paths,'下载后文章图片')
        for index, article_img in enumerate(article_img_list):
            correct_article_img = 'http://cdn.99php.cn' + article_img_paths[index].replace('full', '')
            content = content.replace(article_img, correct_article_img)
        return content


# 下载头像图片
class DownloadHeadImagesPipeline(ImagesPipeline):
    # 下载图片
    def get_media_requests(self, item, info):
        if item['head_img'] != '':
            yield Request(item['head_img'])

    def item_completed(self, results, item, info):
        img_paths = [x['path'] for ok, x in results if ok]
        if not img_paths:
            raise DropItem("Item contains no images")
        item['head_img_paths'] = img_paths
        return item


# 下载文章图片
class DownloadArticleImagesPipeline(ImagesPipeline):
    # 下载图片
    def get_media_requests(self, item, info):
        for article_img in item['article_img_list']:
            yield Request(article_img)

    def item_completed(self, results, item, info):
        img_paths = [x['path'] for ok, x in results if ok]
        if not img_paths:
            raise DropItem("Item contains no images")
        item['article_img_paths'] = img_paths
        return item
