# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from crawlerbot.items import PropertyLinkItem


class hflinkrentSpider(scrapy.Spider):
	name = 'hflinkrentspider'
	output_name = 'hflinkrent'
	custom_settings = {
		'ITEM_PIPELINES': {
			'crawlerbot.pipelines.JsonPipeline': 400
		}
	}
	allowed_domains = ['homefinderbangkok.com']
	start_urls = ['https://homefinderbangkok.com/rentbangkokcondo/page/1']

	BASE_URL = 'https://homefinderbangkok.com/rentbangkokcondo/page/'

	# APPEND_URL = '&Type=Home&Country=%A1%C3%D8%A7%E0%B7%BE%C1%CB%D2%B9%A4%C3&Submit=Search'

	def parse(self, response):
		# last_page = response.xpath('//div[@class="pagination"]/a/text()').extract_first()
		# 385 pages - 29/04/19
		for i in range(1, 385):
			absolute_url = self.BASE_URL + str(i)
			yield scrapy.Request(absolute_url, callback=self.parse_attr)

	def parse_attr(self, response):
		units = response.xpath('//div[@class="title"]')
		for h in units:
			item = PropertyLinkItem()
			item['name'] = h.xpath('a/text()').extract_first()
			item['link'] = h.xpath('a/@href').extract_first()
			yield item
