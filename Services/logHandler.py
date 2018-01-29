import logging


def set_loggers():
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.response').setLevel(logging.WARNING)
    logging.getLogger('telegram').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.contrib.appengine').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.contrib').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.connectionpool').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.util').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.util.retry').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3').setLevel(logging.WARNING)
    logging.getLogger('telegram.bot').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.poolmanager').setLevel(logging.WARNING)
    logging.getLogger('telegram.vendor.ptb_urllib3.urllib3.connection').setLevel(logging.WARNING)
    logging.getLogger('future_stdlib').setLevel(logging.WARNING)


def list_loggers():
    for line in logging.Logger.manager.loggerDict.keys():
        print(line)
