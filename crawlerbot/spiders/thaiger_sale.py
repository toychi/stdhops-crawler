import scrapy

class thaigerSpider(scrapy.Spider):
	name = 'salethaigerspider'
	start_urls = ['https://property.thethaiger.com/property-for-sale/bangkok']

	def parse(self, response):
		SET_SELECTOR = "//div[@class='marker-link list_search']"
		for t in response.xpath(SET_SELECTOR):

			NAME_SELECTOR = './/div[@class="description_search"]/div[@class="hader_title"]/h3/a/text()'
			LOCATION_SELECTOR = './/div[@class="description_search"]/div[@class="hader_title"]/span[@class="location n-table"]/text()'
			ID_SELECTOR = './/div[@class="description_search"]/div[@class="data-list "]/div[@class="tooltipPjax"]/strong/text()'
			TYPE_SELECTOR = './/div[@class="description_search"]/div[@class="hader_title"]/span[@class="type n-photo"]/text()'
			SIZE_SELECTOR = './/div[@class="slide_search"]/div[@class="row bt-detail black-bg n-table"]/div[@class="col-md-12 text-left"]/div[@class="btn-project"]/div[@class="last  "]/strong/span[@class="block-m"]/text()'
			PRICE_SELECTOR = './/div[@class="slide_search"]/div[@class="row bt-detail black-bg n-table"]/div[@class="col-md-12 text-left"]/span[@class="listTotalPrice"]/text()'
			yield {
				'name': t.xpath(NAME_SELECTOR).extract_first(),
				'location': t.xpath(LOCATION_SELECTOR).extract_first(),
				'id': t.xpath(ID_SELECTOR).extract_first(),
				'type': t.xpath(TYPE_SELECTOR).extract_first(),
				'size': t.xpath(SIZE_SELECTOR).extract_first(),
				'saleprice': t.xpath(PRICE_SELECTOR).extract_first(),
			}
			
		NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback=self.parse
			)