import scrapy

class thaisrcSpider(scrapy.Spider):
	name = 'thaisrcspider'
	start_urls = ['http://www.thairsc.com/p77/index/10']

	def parse(self, response):
		SET_SELECTOR = "//div[@class='panel-body']"
		for t in response.xpath(SET_SELECTOR):

			LOCATION_SELECTOR = 'table/tr/td/a/text()'
			ACCIDENT_SELECTOR = '//table[@class="table"]/tbody/tr/td[@class="text-center text-danger"]/text()'
			D_SELECTOR = 'table/tr/td[@class="text-center text-success"]/span[@class="td-data-dead"]/text()'
			INJ_SELECTOR = 'table/tr/td[@class="text-center text-danger"]/span[@class="td-data-inj"]/text()'
			T_SELECTOR = 'table/tr/td[@class="text-center text-primary"]/span[@class="td-data-total"]/text()'
			yield {
				'location': t.xpath(LOCATION_SELECTOR).extract_first(),
				'accident': t.xpath(ACCIDENT_SELECTOR).extract_first(),
				'dead': t.xpath(D_SELECTOR).extract_first(),
				'injure': t.xpath(INJ_SELECTOR).extract_first(),
				'total': t.xpath(T_SELECTOR).extract_first(),
			}