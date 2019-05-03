# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from crawlerbot.items import PropertyLinkItem


class tglinksaleSpider(scrapy.Spider):
	name = 'tglinksalespider'
	output_name = 'tglinksale'
	custom_settings = {
		'ITEM_PIPELINES': {
			'crawlerbot.pipelines.JsonPipeline': 400
		}
	}
	allowed_domains = ['property.thethaiger.com']
	start_urls = ['https://property.thethaiger.com/property-for-sale/bangkok?lng=en&zoom=12&hide_similar=1&available_unit=1&mapOnOff=off&page=1&per-page=20']

	BASE_URL = 'https://property.thethaiger.com/property-for-sale/bangkok?lng=en&zoom=12&hide_similar=1&available_unit=1&mapOnOff=off&page='

	APPEND_URL = '&per-page=20'

	def parse(self, response):
		# 139 pages - 29/04/19
		for i in range(1, 139):
			absolute_url = self.BASE_URL + str(i) + self.APPEND_URL
			yield scrapy.Request(absolute_url, callback=self.parse_attr)

	def parse_attr(self, response):
		units = response.xpath('//div[@class="description_search"]/div[@class="hader_title"]/h3')
		for h in units:
			item = PropertyLinkItem()
			item['name'] = h.xpath('a/text()').extract_first()
			item['link'] = 'https://property.thethaiger.com' + h.xpath('a/@href').extract_first()
			item['pid'] = item['link'].split('-')[-2].upper() + '-' + item['link'].split('-')[-1]
			item['maps'] = "https://property.thethaiger.com/get-map/unit/" + item['pid']
			yield item
