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
        jsonresponse = json.loads(response.body_as_unicode())   
        jsonbody = {}
        jsonbody = jsonresponse["body"]
        for city in jsonbody:
            yield Request(urls.town_index.format(city["CODE"]), callback=self.parse_town)

    def parse_town(self, response):
        city_code = extract_url(response.url, 'cityCode')
        hxs = HtmlXPathSelector(response)
        rows = hxs.xpath('//tbody/tr')
        for row in range(1, len(rows)+1):
            city_code=city_code
            district_name=extract_candidacy_field(hxs,row,1)
            county_name=extract_candidacy_field(hxs,row,2)[0]
            town_names=extract_candidacy_field(hxs,row,3)[0].split(',')
            for town_name in town_names:
                yield items.TownItem(
                    cityCode=city_code,
                    districtName=district_name,
                    townName=county_name+" "+town_name.strip()
                )    
            