# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class popongKeywordSpider(BaseSpider):

    name = 'popongKeywordSpider'

    def start_requests(self):
        yield Request(urls.popong_index, method='GET')
        

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        ids = extract_ids_for_popong(hxs, 'person')
        for id in ids:
            yield Request(urls.popong_person % id, callback=self.parse_member_info)

    def parse_member_info(self, response):
        hxs = HtmlXPathSelector(response)
        name = extract_popong_name(hxs)
        birth = extract_popong_birth(hxs)
        keywordList = extract_popong_keywords(hxs)
        for keywordStr in keywordList:
            keywordSet = keywordStr.split(':')
            keyword_size = keywordSet[1].replace('"'," ").strip()
            keyword_name = u'"%s"' % keywordSet[0].replace('"'," ").strip()
            yield items.BillKeywords(name=name,birth=birth,keyword_name = json.loads(keyword_name),keyword_size=keyword_size)