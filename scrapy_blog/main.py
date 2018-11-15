from scrapy import cmdline
from scrapy_blog import log

log.msg('开始爬虫', '开始')
cmdline.execute('scrapy crawl cnblogs_spider'.split())
log.msg('结束爬虫', '结束')