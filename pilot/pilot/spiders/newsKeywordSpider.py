# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

from collections import Counter
import urllib
import random
import webbrowser
import xml.etree.ElementTree as ET
import httplib

from konlpy.tag import Hannanum
from lxml import html
import pytagcloud # requires Korean font support
import sys


class newsKeywordSpider(BaseSpider):
    name = 'newsKeywordSpider'

    def get_news_text(self,query):
        params = urllib.urlencode({'query': query, 'display': 10, 'start': 1})
        headers = {"X-Naver-Client-Id": "TsshNF_3sY3pu9gOkU7d","X-Naver-Client-Secret": "5FOHV3Ysqo"}
        conn = httplib.HTTPSConnection("openapi.naver.com")
        url = '/v1/search/news.xml?query=%s&display=10&start=1&sort=sim' % urllib.quote_plus(query)
        conn.request("GET", url ,params, headers)
        response = conn.getresponse()
        root = ET.fromstring(response.read())
        newsText = ''
        for link in root.iter('link'):
            code   = urllib.urlopen(link.text).read()
            htmlCode = html.fromstring(code)
            results = htmlCode.xpath('//div[@id="articleBodyContents"]/text()')
            for result in results:
                newsText += result.strip()
        print(newsText)
        return newsText
        

    def get_tags(self,text, ntags=20, multiplier=10):
        h = Hannanum()
        nouns = h.nouns(text)
        count = Counter(nouns)
        return [{'tag': n, 'size': c*multiplier }\
                    for n, c in count.most_common(ntags)]

    def start_requests(self):
        yield Request(urls.candidacy_index.format(-1,-1), method='POST')

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.xpath('//tbody/tr')
        for row in range(1, len(rows)+1):
            candidacy_id=extract_candidacy_id(hxs,row)
            candidacy_name=extract_candidacy_name(hxs,row)
            query = candidacy_name.encode('utf-8') + "후보"
            text = self.get_news_text(query)
            tags = self.get_tags(text)
            for tag in tags:
                yield items.AssemblyNewsKeyword(candidacy_id=candidacy_id,keyword_name=tag['tag'].encode('utf-8'),keyword_size=tag['size'])

