from scrapy import cmdline
from scrapy_blog.log import msg

msg('开始采集！')
cmdline.execute('scrapy crawl cnblogs_spider'.split())
msg('结束采集')
