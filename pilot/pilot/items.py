# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CityItem(Item):
	city_name=Field()
	city_code=Field()

class DistrictItem(Item):
	city_code=Field()
	district_name=Field()
	district_code=Field()

class CandidacyItem(Item):
	candidacy_id=Field()
	candidacy_img=Field()
	district_code=Field()
	party=Field()
	name=Field()
	gender=Field()
	birth=Field()
	address=Field()
	education=Field()
	experience=Field()
	criminal=Field()

class AssemblyMemberItem(Item):
	assembly_id=Field()
	name=Field()
	birthYear=Field()
	attendance_rate=Field()
	proposal=Field()

class AssemblyNewsKeyword(Item):
	keyword_id=Field()
	candidacy_id=Field()
	keyword_name=Field()
	keyword_size=Field()


class BillKeywords(Item):
	name=Field()
	birth=Field()
	keyword_name=Field()
	keyword_size=Field()