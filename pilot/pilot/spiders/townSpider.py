# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class townSpider(BaseSpider):
    name = 'townSpider'

    def start_requests(self):
        yield Request(urls.city_index, method='GET')

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        cityCodes = extract_cityCodes(hxs)
        cityNames = extract_cityNames(hxs)
        for code, name in zip(cityCodes, cityNames):
            yield Request(urls.town_index % code, callback=self.parse_town)

    def parse_town(self, response):
        id = extract_url(response.url, 'cityCode')
        jsonresponse = json.loads(response.body_as_unicode())
        jsonbody = {}
        jsonbody = jsonresponse["body"]
        for town in jsonbody:
        	yield items.townItem(city_code=id,town_name=town["NAME"],town_code=town["CODE"])