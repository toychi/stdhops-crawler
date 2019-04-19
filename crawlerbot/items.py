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


class PropertyLinkItem(scrapy.Item):
    pid = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    maps = scrapy.Field()

    
class TgItem(scrapy.Item):
    pid = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    ptype = scrapy.Field()
    area = scrapy.Field()
    size = scrapy.Field()
    floor = scrapy.Field()
    yearbuilt = scrapy.Field()
    price = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    furniture = scrapy.Field()
    daypost = scrapy.Field()
    latlng = scrapy.Field()