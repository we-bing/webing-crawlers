# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class assemblyMemberSpider(BaseSpider):

    name = 'assemblyMemberSpider'

    def start_requests(self):
        yield Request(urls.member_index, method='POST')
        yield Request(urls.private % id, callback=self.parse_private)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        ids = extract_ids(hxs, 'member_seq')
        names = extract_texts(hxs, 'member_seq')
        for id, name in zip(ids, names):
            tempText = name.encode('utf-8').split('(')
            realName = tempText[0].strip()
            callback4report = lambda response,item=items.AssemblyMemberItem(assembly_id=id, name=realName): self.parse_report(response,item)
            # yield items.AssemblyMemberItem(assembly_id=id, name=realName)
            yield Request(urls.member_report % id,callback=callback4report)

    def parse_report(self, response, receivedItem):
        id = extract_url(response.url, 'member_seq')
        item = receivedItem;
        hxs = HtmlXPathSelector(response)
        attendance_rate = extract_integer(hxs, xpaths.member_report_for_attendance_rate)
        proposal = extract_integer(hxs, xpaths.member_report_for_proposal)
        item['attendance_rate'] = attendance_rate
        item['proposal'] = proposal
        callback4birth = lambda response,item=item: self.parse_birth(response,item)
        yield Request(urls.member_birth % id,callback=callback4birth)

    def parse_birth(self, response, receivedItem):
        item = receivedItem;
        hxs = HtmlXPathSelector(response)
        birthYear = extract_integer(hxs, xpaths.member_birth)
        item['birthYear'] = birthYear
        yield item