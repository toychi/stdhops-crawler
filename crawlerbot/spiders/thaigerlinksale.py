# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from crawlerbot.items import ThaigerlinkItem


class thaigerlinksaleSpider(scrapy.Spider):
	name = 'tglinksalespider'
	file_name = 'tglinksale.json'
	custom_settings = {
		'ITEM_PIPELINES': {
			'crawlerbot.pipelines.LinksPipeline': 400
		}
	}
	allowed_domains = ['property.thethaiger.com']
	start_urls = ['https://property.thethaiger.com/property-for-sale/bangkok?lng=en&zoom=12&hide_similar=1&available_unit=1&mapOnOff=off&page=1&per-page=20']

	BASE_URL = 'https://property.thethaiger.com/property-for-sale/bangkok?lng=en&zoom=12&hide_similar=1&available_unit=1&mapOnOff=off&page='

	APPEND_URL = '&per-page=20'

	def parse(self, response):
		# last_page = response.xpath('//div[@class="pagination"]/a/text()').extract_first()138
		# for i in range(1, 138):
		for i in range(1, 8):
			absolute_url = self.BASE_URL + str(i) + self.APPEND_URL
			yield scrapy.Request(absolute_url, callback=self.parse_attr)

	def parse_attr(self, response):
		units = response.xpath('//div[@class="description_search"]/div[@class="hader_title"]/h3')
		for h in units:
			item = ThaigerlinkItem()
			item['name'] = h.xpath('a/text()').extract_first()
			item['link'] = h.xpath('a/@href').extract_first()
			yield item
