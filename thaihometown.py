import scrapy
import json

class thTownSpider(scrapy.Spider):
	name = 'thtownspider'
	with open("thaihometown.json", 'r') as infile:
		contents = json.load(infile)

	links_list = []
	links_list = list(set(links_list))

	def parse(self, response):
		SET_SELECTOR = '.description_search'
		for t in response.css(SET_SELECTOR):

			NAME_SELECTOR = 'h2 a ::text'
			LOCATION_SELECTOR = './/span[@class="location n-table"]/text()'
			ID_SELECTOR = './/div[@class="tooltipPjax"]/strong/text()'
			TYPE_SELECTOR = './/span[@class="type n-photo"]/text()'
			SIZE_SELECTOR = './/div[@class="last  "]/text()'
			PRICE_SELECTOR = './/span[@class="listTotalPrice"]/text()'
			TRANSPORT_SELECTOR = './/div[/text() = "To BTS: "]/strong/text()'
			yield {
				'name': t.css(NAME_SELECTOR).extract_first(),
				'location': t.xpath(LOCATION_SELECTOR).extract_first(),
				'id': t.xpath(ID_SELECTOR).extract_first(),
				'type': t.xpath(TYPE_SELECTOR).extract_first(),
				'size': t.xpath(SIZE_SELECTOR).extract_first(),
				'saleprice': t.xpath(PRICE_SELECTOR).extract_first(),
				'btsdis': t.xpath(TRANSPORT_SELECTOR).extract_first(),
			}
			

		#NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
		#next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		#if next_page:
		#	yield scrapy.Request(
		#		response.urljoin(next_page),
		#		callback=self.parse
		#	)