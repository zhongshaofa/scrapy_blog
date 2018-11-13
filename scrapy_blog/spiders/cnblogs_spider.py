# -*- coding: utf-8 -*-
import scrapy
from scrapy_blog.items import ScrapyBlogItem


class CnblogsSpiderSpider(scrapy.Spider):
    name = 'cnblogs_spider'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']

    def parse(self, response):
        list = response.xpath("//div[@id='post_list']//div[@class='post_item']")
        for item in list:
            blog_item = ScrapyBlogItem()
            blog_item['title'] = item.xpath(".//h3/a/text()").extract_first()
            blog_item['url'] = item.xpath(".//h3/a/@href").extract_first()
            blog_item['describe'] = item.xpath(
                "normalize-space(.//p[@class='post_item_summary']//text())").extract_first()
            blog_item['head_img'] = item.xpath(".//p/a/img[@class='pfs']/@src").extract_first()
            blog_item['praise'] = item.xpath(".//span[@class='diggnum']//text()").extract_first()
            blog_item['author'] = item.xpath(".//div//a[@class='lightblue']//text()").extract_first()
            blog_item['clicks'] = item.xpath(".//div//span[@class='article_view']//a/text()").extract_first()
            self.correct_item(blog_item)
            # blog_item['create_time'] = item.xpath(".//div[@class='post_item_foot']//text()").extract_first()
            # print(blog_item)
            yield scrapy.Request(url=blog_item['url'], meta={'items': blog_item}, callback=self.parse_content,
                                 dont_filter=True)

    # 爬取文章内容
    def parse_content(self, response):
        blog_item = response.meta['items']
        blog_item['content'] = response.xpath("//div//div[@id='cnblogs_post_body']").extract_first()
        print(blog_item)
        # items['time'] = response.xpath('//div[@class="jbqk"]/ul/li[5]/text()')[0].extract()
        # items['detail_content'] = response.xpath('//div[@class="tsnr"]/p/text()')[0].extract()
        # items['Reply'] = response.xpath('//div[@class="tshf"]/p/text()')[0].extract()
        # yield items

    # 修正数据
    def correct_item(self, items):
        for item in items:
            if items[item] is None:
                items[item] = ''
                items[item].strip()
        items['head_img'] = "http:" + items['head_img']
        return items
