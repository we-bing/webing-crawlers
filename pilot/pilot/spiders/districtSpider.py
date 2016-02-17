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
        hxs = HtmlXPathSelector(response)
        cityCodes = extract_cityCodes(hxs)
        for code in cityCodes:
            yield Request(urls.district_index % code, callback=self.parse_district)

    def parse_district(self, response):
        city_code = extract_url(response.url, 'cityCode')
        jsonresponse = json.loads(response.body_as_unicode())
        jsonbody = {}
        jsonbody = jsonresponse["body"]
        for district in jsonbody:
        	yield items.DistrictItem(city_code=city_code,district_name=district["NAME"],district_code=district["CODE"])