# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

import MySQLdb



class assemblyReportSpider(BaseSpider):

    name = 'assemblyReportSpider'


    def start_requests(self):
        # Open database connection
        db = MySQLdb.connect("localhost","root","","webingpilot" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        try:
            # execute SQL query using execute() method.
            cursor.execute("SELECT assembly_id FROM ASSEMBLY_MEMBERS")

            results = cursor.fetchall()

            for row in results:
                yield Request(urls.member_private % row[0], callback=self.parse)

            db.commit()
        except:
            db.rollback()
        # disconnect from server
        db.close()

    def parse(self, response):
        # db = MySQLdb.connect("localhost","root","","webingpilot" )
        # cursor = db.cursor()
        id = extract_url(response.url, 'member_seq')
        hxs = HtmlXPathSelector(response)
        attendance_rate = extract_integer(hxs, xpaths.member_report_for_attendance_rate)
        proposal = extract_integer(hxs, xpaths.member_report_for_proposal)
        print(id)
        print(attendance_rate)
        print(proposal)
        # print "update assembly member's %d report %d %d" % (id, attendance_rate,proposal)
        # cursor.execute("UPDATE ASSEMBLY_MEMBERS SET attendance_rate = %d, proposal = %d WHERE assembly_id = %d" % (attendance_rate[0],proposal[0],id))

        