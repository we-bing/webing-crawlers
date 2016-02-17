# -*- coding: utf-8 -*-

import re
import itertools
import lxml.html

__all__ = ["convert_to_text","extract_cityCodes","extract_cityNames","extract_url","extract_candidacy_field","extract_candidacy_id","extract_candidacy_img","extract_candidacy_name"]


def convert_to_text(e):
    texts = []
    texts.append(e.text.strip())
    for br in e:
        assert br.tag == 'br'
        texts.append('\n')
        if e.tail: texts.append(e.tail.strip())
    return ''.join(texts)


def extract_cityCodes(hxs):
    xpath = '//select[@id="cityCode"]/option/@value'
    return hxs.select(xpath).extract()

def extract_cityNames(hxs):
    xpath = '//select[@id="cityCode"]/option/text()'
    return hxs.select(xpath).extract()

def extract_url(url, key):
    return re.search(r'%s=(((-)\d+)|(\d+))' % key, url).group(1)

def extract_candidacy_field(hxs, row, idx):
	xpath = '//tbody/tr[%s]/td[%s]/text()' % (row,idx)
	return hxs.select(xpath).extract()

def extract_candidacy_id(hxs, row):
	xpath = '//tbody/tr[%s]/td/img/@src' % row
	result = hxs.select(xpath).re(r'(\d+).jpg')
	return result[0]

def extract_candidacy_img(hxs, row):
	xpath = '//tbody/tr[%s]/td/img/@src' % row
	result = hxs.select(xpath).extract()
	return result[0]

def extract_candidacy_name(hxs, row): 
	xpath = '//tbody/tr[%s]/td[4]/a/text()' % row
	result = hxs.select(xpath).extract()
	return result[0].strip()

	
	