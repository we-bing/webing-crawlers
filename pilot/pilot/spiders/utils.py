# -*- coding: utf-8 -*-

import re
import itertools
import lxml.html

__all__ = ["extract_proposal","extract_attendance_rate","convert_to_text","extract_cityCodes","extract_cityNames","extract_url","extract_candidacy_field","extract_candidacy_id","extract_candidacy_img","extract_candidacy_name","extract_ids","extract_texts","extract_integer","extract_news_contents","extract_ids_for_popong","extract_popong_name","extract_popong_keywords","extract_popong_birth"]


def convert_to_text(e):
    texts = []
    texts.append(e.text.strip())
    for br in e:
        assert br.tag == 'br'
        texts.append('\n')
        if e.tail: texts.append(e.tail.strip())
    return ''.join(texts)

def extract_attendance_rate(hxs):
    xpath = '//span[@style="color:#23C6C8"]/text()'
    result = hxs.select(xpath).re(r'(?:\d*\.)?\d+')
    return result[1]

def extract_proposal(hxs):
    xpath = '//span[@style="color:#23C6C8"]/text()'
    result = hxs.select(xpath).re(r'(?:\d*\.)?\d+')
    return result[0]

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
    xpath = '//tbody/tr[%s]/td[5]/a/@id' % row
    # result = hxs.select(xpath).re(r'(\d+).(JPG|jpg|gif|GIF|jpeg|JPEG)')
    result = hxs.select(xpath).extract()
    if not result: return ''
    return result[0]

def extract_candidacy_img(hxs, row):
    xpath = '//tbody/tr[%s]/td/input[@type="image"]/@src' % row
    result = hxs.select(xpath).extract()
    if not result: return ''
    return result[0]

def extract_candidacy_name(hxs, row): 
    xpath = '//tbody/tr[%s]/td[5]/a/text()' % row
    result = hxs.select(xpath).extract()
    if not result: return ''
    return result[0].strip()

def extract_ids(hxs, key):
    xpath = '//a[contains(@href, "%s=")]/@href' % key
    return hxs.select(xpath).re(r'%s=(\d+)' % key)

def extract_texts(hxs, key):
    xpath = '//a[contains(@href, "%s=")]/text()' % key
    return hxs.select(xpath).extract()

def extract_integer(hxs, xpath):
    result = hxs.select(xpath).re(r'(?:\d*\.)?\d+')
    if not result: return ''
    return result[0]

def extract_news_contents(hxs):
    xpath = "//div[@id='articleBodyContents']/text()"
    result = hxs.select(xpath).extract()
    return convert_to_text(lxml.html.fromstring(result[0]))

def extract_ids_for_popong(hxs, key):
    xpath = '//a[contains(@href, "/%s/")]/@href' % key
    return hxs.select(xpath).re(r'/%s/(\d+)' % key)

def extract_popong_name(hxs):
    xpath = '//a[@class="person-name"]/text()'
    return hxs.select(xpath).extract()

def extract_popong_birth(hxs):
    xpath = '//a[contains(@href, "/entity/")]/text()'
    return hxs.select(xpath).extract()

def extract_popong_keywords(hxs):
    xpath = '//div[@class="person-summary-vis"]/script[5]/text()'
    scriptText = hxs.select(xpath).re(r'{(.*)},')
    tagList = scriptText[0].split(',')
    return tagList



	
	