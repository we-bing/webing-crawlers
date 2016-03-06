# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class districtSpider(BaseSpider):
    name = 'districtSpider'

    def start_requests(self):
        yield Request(urls.city_index, method='GET')

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        jsonbody = {}
        jsonbody = jsonresponse["body"]
        for city in jsonbody:
            yield Request(urls.district_index % city["CODE"], callback=self.parse_district)

    def parse_district(self, response):
        city_code = extract_url(response.url, 'cityCode')
        jsonresponse = json.loads(response.body_as_unicode())
        jsonbody = {}
        jsonbody = jsonresponse["body"]
        for district in jsonbody:
        	yield items.DistrictItem(cityCode=city_code,districtName=district["NAME"],districtCode=district["CODE"])