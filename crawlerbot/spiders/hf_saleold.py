import scrapy

class homefinderSpider(scrapy.Spider):
	name = 'salehfspider'
	start_urls = ['https://homefinderbangkok.com/buybangkokcondo/']

	def parse(self, response):
		SET_SELECTOR = '.property'
		for t in response.css(SET_SELECTOR):

			NAME_SELECTOR = './/div[@class="title"]/a/text()'
			#LOCATION_SELECTOR = './/div[@class="footer"]/text()'
			TYPE_SELECTOR = './/div[@class="icon type"]/text()'
			SIZE_SELECTOR = './/div[@class="icon size"]/text()'
			PRICE_SELECTOR = './/div[@class="price"]/text()'
			yield {
				'name': t.xpath(NAME_SELECTOR).extract_first(),
				#'location': t.xpath(LOCATION_SELECTOR).extract_first(),
				'type': t.xpath(TYPE_SELECTOR).extract_first(),
				'size': t.xpath(SIZE_SELECTOR).extract_first(),
				'saleprice': t.xpath(PRICE_SELECTOR).extract_first(),
			}
			
		NEXT_PAGE_SELECTOR = '//div[@class="pagination"]/a[contains(text(),"Next")]/@href'
		next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback=self.parse
			)