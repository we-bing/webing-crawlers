# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class candidacySpider(BaseSpider):
    name = 'candidacySpider'

    def start_requests(self):
        yield Request(urls.city_index, method='GET')
#bizcommon/selectbox/selectbox_getSggCityCodeJson.json?electionId=0020160413&electionCode=2&cityCode=%s -1 하면 시티코드 불필요.
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        cityCodes = extract_cityCodes(hxs)
        for code in cityCodes:
            if int(code) == -1:
                continue
            yield Request(urls.district_index % code, callback=self.parse_district)

            

    def parse_district(self, response):
        city_code = extract_url(response.url, 'cityCode')
        jsonresponse = json.loads(response.body_as_unicode())
        jsonbody = {}
        jsonbody = jsonresponse["body"]
        for district in jsonbody:
            yield Request(urls.candidacy_index.format(city_code,district["CODE"].encode('utf-8')) , callback=self.parse_candidacy)

    def parse_candidacy(self, response):
        district_code = extract_url(response.url, 'sggCityCode')
        hxs = HtmlXPathSelector(response)
        rows = hxs.xpath('//tbody/tr')
        for row in range(1, len(rows)+1):
            candidacy_id=extract_candidacy_id(hxs,row)
            candidacy_img=extract_candidacy_img(hxs,row)
            district_code=district_code
            party=extract_candidacy_field(hxs,row,2)
            name=extract_candidacy_name(hxs,row)
            gender=extract_candidacy_field(hxs,row,5)
            birth=extract_candidacy_field(hxs,row,6)
            address=extract_candidacy_field(hxs,row,7)
            education=extract_candidacy_field(hxs,row,9)
            experience=extract_candidacy_field(hxs,row,10)
            criminal=extract_candidacy_field(hxs,row,11)
            if len(candidacy_id.strip()) < 1:
                print("need to confirm !!"+name+district_code)
            yield items.CandidacyItem(
                    candidacy_id=candidacy_id,
                    candidacy_img=candidacy_img,
                    district_code=district_code,
                    party=party,
                    name=name,
                    gender=gender,
                    birth=birth,
                    address=address,
                    education=education,
                    experience=experience,
                    criminal=criminal
                )