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
    	jsonresponse = json.loads(response.body_as_unicode())	
        jsonbody = {}
        jsonbody = jsonresponse["body"]
        for city in jsonbody:
            yield items.CityItem(city_code=city["CODE"], city_name=city["NAME"])