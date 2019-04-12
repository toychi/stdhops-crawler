import scrapy
from crawlerbot.items import TgItem
import json
import re


class thaigerrentSpider(scrapy.Spider):
    name = 'tgrentspider'
    collection_name = 'tgrent'

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlerbot.pipelines.MongoPipeline': 400
        }
        # 'LOG_FILE': 'crawlerbot/logs/demospider.log',
        # 'LOG_LEVEL': 'DEBUG'
    }

    with open('crawlerbot/links/tglinkrent.json', 'r') as f:
        data = json.load(f)
        urls = [d['link'] for d in data]
        start_urls = urls

    def parse(self, response):
        item = TgItem()
        item['id'] = response.xpath('//div[@class="unit_id"]/strong/text()').extract_first()
        item['name'] = response.xpath('//h2[@class="project_title"]/a/text()').extract_first()
        item['location'] = response.xpath('//ul[@class="basic-list"]/li/strong/text()').extract()[1]
        item['type'] = response.xpath('//ul[@class="basic-list"]/li/strong/text()').extract()[0]
        item['size'] = response.xpath('//div[@class="txt"]/strong/text()').extract()[2]
        item['floor'] = response.xpath('//div[@class="details_unit_floor"]/text()').extract_first()
        item['yearbuilt'] = response.xpath('//ul[@class="basic-list"]/li/strong[contains(text(),"Completed")]/text()').extract_first()
        item['price'] = response.xpath('//span[@class="unit_price"]/text()').extract_first()[1:]
        item['bed'] = response.xpath('//div[@class="txt"]/strong/text()').extract_first()
        item['bath'] = response.xpath('//div[@class="txt"]/strong/text()').extract()[1]
        item['furniture'] = response.xpath('//ul[@class="basic-list"]/li/strong[contains(text(),"Furnished")]/text()').extract_first()
        item['daypost'] = response.xpath('//li[@class="hidden-sm hidden-xs"]/text()').extract_first()
        #t = response.xpath('//div[@class="gs-wrapper"]/script').extract()[0]
        #latlng = re.findall(r'parseFloat\((.+)\);', t)
        #item['latlng'] = [latlng[0], latlng[1]]
        return item
        
