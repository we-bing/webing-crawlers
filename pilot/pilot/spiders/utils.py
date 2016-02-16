import re
import itertools
import lxml.html

__all__ = ["extract_cityCodes","extract_cityNames","extract_url"]

def extract_cityCodes(hxs):
    xpath = '//select[@id="cityCode"]/option/@value'
    return hxs.select(xpath).extract()

def extract_cityNames(hxs):
    xpath = '//select[@id="cityCode"]/option/text()'
    return hxs.select(xpath).extract()

def extract_url(url, key):
    return re.search(r'%s=(\d+)' % key, url).group(1)
