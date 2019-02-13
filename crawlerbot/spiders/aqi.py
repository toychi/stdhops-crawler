import scrapy
from crawlerbot.items import aqiItem

class aqiSpider(scrapy.Spider):
	name = 'aqispider'
	start_urls = ['http://aqicn.org/city/bangkok/']

	def parse(self, response):
		units = response.xpath("//script[contains(., 'stations')]")
		for h in units:
			item = aqiItem()
			item['aqi'] = h.xpath('/text[contains(., "aqi")]').extract_first()
			item['city'] = h.xpath('/text[contains(., "city")]').extract_first()
			yield item