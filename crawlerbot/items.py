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


class HouseLinkItem(scrapy.Item):
    id = scrapy.Field()
    
class ThaihometownItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    maps = scrapy.Field()


class RenthomefinderItem(scrapy.Item):
    maps = scrapy.Field()
    link = scrapy.Field()


class HouseItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    room = scrapy.Field()
    district = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    latlng = scrapy.Field()
    date = scrapy.Field()

    
class HflinkItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()


class HfItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    latlng = scrapy.Field()


class ThaigerlinkItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()

	
class TgItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    latlng = scrapy.Field()