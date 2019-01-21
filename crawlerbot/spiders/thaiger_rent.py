import scrapy

class thaigerSpider(scrapy.Spider):
	name = 'thaigerspider'
	start_urls = ['https://property.thethaiger.com/property-for-rent/bangkok']

	def parse(self, response):
		SET_SELECTOR = '.description_search'
		for t in response.css(SET_SELECTOR):

			NAME_SELECTOR = 'h3 a ::text'
			LOCATION_SELECTOR = './/span[@class="location n-table"]/text()'
			ID_SELECTOR = './/div[@class="tooltipPjax"]/strong/text()'
			TYPE_SELECTOR = './/span[@class="type n-photo"]/text()'
			SIZE_SELECTOR = './/strong/span[@class="block-m"]//text()'
			RENTAL_SELECTOR = './/span[@class="listTotalPrice"]/text()'
			#TRANSPORT_SELECTOR = './/div[/text() = "To BTS: "]/strong/text()'
			yield {
				'name': t.css(NAME_SELECTOR).extract_first(),
				'location': t.xpath(LOCATION_SELECTOR).extract_first(),
				'id': t.xpath(ID_SELECTOR).extract_first(),
				'type': t.xpath(TYPE_SELECTOR).extract_first(),
				'size': t.xpath(SIZE_SELECTOR).extract_first(),
				'rentprice': t.xpath(RENTAL_SELECTOR).extract_first(),
				#'btsdis': t.xpath(TRANSPORT_SELECTOR).extract_first(),
			}
			

		#NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
		#next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		#if next_page:
		#	yield scrapy.Request(
		#		response.urljoin(next_page),
		#		callback=self.parse
		#	)