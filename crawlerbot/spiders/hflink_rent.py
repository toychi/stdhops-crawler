# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from crawlerbot.items import HflinkItem


class hflinkrentSpider(scrapy.Spider):
	name = 'hflinkrentspider'
	allowed_domains = ['homefinderbangkok.com']
	start_urls = ['https://homefinderbangkok.com/rentbangkokcondo/page/1']

	BASE_URL = 'https://homefinderbangkok.com/rentbangkokcondo/page/'
	#APPEND_URL = '&Type=Home&Country=%A1%C3%D8%A7%E0%B7%BE%C1%CB%D2%B9%A4%C3&Submit=Search'


	def parse(self, response):
		#last_page = response.xpath('//div[@class="pagination"]/a/text()').extract_first()
		for i in range(1, 367):
			absolute_url = self.BASE_URL + str(i)
			yield scrapy.Request(absolute_url, callback=self.parse_attr)

	def parse_attr(self, response):
		units = response.xpath('//div[@class="title"]')
		for h in units:
			item = HflinkItem()
			item['name'] = h.xpath('a/text()').extract_first()
			item['link'] = h.xpath('a/@href').extract_first()
			yield item
