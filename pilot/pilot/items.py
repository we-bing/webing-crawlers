# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CityItem(Item):
	city_name=Field()
	city_code=Field()

class districtItem(Item):
	city_code=Field()
	district_name=Field()
	district_code=Field()