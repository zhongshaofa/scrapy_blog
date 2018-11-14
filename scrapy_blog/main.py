from scrapy import cmdline
from scrapy_blog import log

log.msg('这是在测试打印日志','日志')
# cmdline.execute('scrapy crawl cnblogs_spider'.split())