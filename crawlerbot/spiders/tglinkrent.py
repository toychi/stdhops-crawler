# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from crawlerbot.items import PropertyLinkItem


class tglinkrentSpider(scrapy.Spider):
	name = 'tglinkrentspider'
	output_name = 'tglinkrent'
	custom_settings = {
		'ITEM_PIPELINES': {
			'crawlerbot.pipelines.JsonPipeline': 400
		}
	}
	allowed_domains = ['property.thethaiger.com']
	start_urls = ['https://property.thethaiger.com/property-for-rent/bangkok?lng=en&zoom=12&hide_similar=1&available_unit=1&mapOnOff=off&page=1&per-page=20']

	BASE_URL = 'https://property.thethaiger.com/property-for-rent/bangkok?lng=en&zoom=12&hide_similar=1&available_unit=1&mapOnOff=off&page='

	APPEND_URL = '&per-page=20'

	def parse(self, response):
		# for i in range(1, 182):
		for i in range(1, 10):
			absolute_url = self.BASE_URL + str(i) + self.APPEND_URL
			yield scrapy.Request(absolute_url, callback=self.parse_attr)

	def parse_attr(self, response):
		units = response.xpath('//div[@class="description_search"]/div[@class="hader_title"]/h3')
		for h in units:
			item = PropertyLinkItem()
			item['name'] = h.xpath('a/text()').extract_first()
			item['link'] = h.xpath('a/@href').extract_first()
			item['pid'] = item['link'].split('-')[-2].upper() + '-' + item['link'].split('-')[-1]
			item['maps'] = "https://property.thethaiger.com/get-map/unit/" + item['pid']
			yield item
