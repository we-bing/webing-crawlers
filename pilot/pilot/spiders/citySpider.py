# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class citySpider(BaseSpider):
    name = 'citySpider'

    def start_requests(self):
        yield Request(urls.city_index, method='GET')

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        cityCodes = extract_cityCodes(hxs)
        cityNames = extract_cityNames(hxs)
        for code, name in zip(cityCodes, cityNames):
            yield items.CityItem(city_code=code, city_name=name)