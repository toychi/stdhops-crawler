import scrapy
import json

class aqiSpider(scrapy.Spider):
	name = 'aqispider'
	start_urls = ['http://aqicn.org/city/bangkok/']

	def parse(self, response):
		#aqi = json.loads(response.xpath("//script[contains(., 'stations')]").extract_first()[94:4445])
		with open('aqi.json','a') as outfile:
			json.dump(response.xpath("//script[contains(., 'stations')]").extract_first()[94:4445], outfile)