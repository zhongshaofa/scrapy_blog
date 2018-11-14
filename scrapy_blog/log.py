import time
import logging
from scrapy.utils.log import configure_logging


# 日志打印
def msg(msg, remark=None):
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename=day + '.log',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )
    if remark is None:
        logging.info('==========================【时间】' + date + '==========================')
    else:
        logging.info('==========================【时间】' + date + '====【备注】' + remark + '==========================')
    logging.info(msg)
