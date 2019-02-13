# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ThaihometownItem(scrapy.Item):
    name = scrapy.Field()
    maps = scrapy.Field()
	
class RenthomefinderItem(scrapy.Item):
    maps = scrapy.Field()

class aqiItem(scrapy.Item):
	aqi = scrapy.Field()
	city = scrapy.Field()