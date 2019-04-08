import scrapy
from crawlerbot.items import HfItem
import json
import re


class homefinderSpider(scrapy.Spider):
    name = 'hfsalecrawlspider'
    collection_name = 'hfsale'

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlerbot.pipelines.MongoPipeline': 400
        }
        # 'LOG_FILE': 'crawlerbot/logs/demospider.log',
        # 'LOG_LEVEL': 'DEBUG'
    }

    with open('crawlerbot/links/hflinksale.json', 'r') as f:
        data = json.load(f)
        urls = [d['link'] for d in data]
        start_urls = urls

    def parse(self, response):
        item = HfItem()
        item['id'] = response.xpath('//div[@class="wrap clearfix"]/h4/text()').extract_first()[15:22]
        item['name'] = response.xpath('//div[@class="propertyname"]/text()').extract_first()[1:]
        item['type'] = response.xpath('//div[@class="wrap clearfix"]/h5/span/small/text()').extract()[0][3:]
        item['size'] = response.xpath('//div[@class="property-meta clearfix"]/span/text()').extract()[0][1:]
        item['price'] = response.xpath('//div[@class="wrap clearfix"]/h5/span/text()').extract()[1][1:]
        item['bed'] = response.xpath('//div[@class="property-meta clearfix"]/span/text()').extract()[1][1:]
        item['bath'] = response.xpath('//div[@class="property-meta clearfix"]/span/text()').extract()[2][1:]
        t = response.xpath('//div[@class="map-wrap clearfix"]/script').extract()[0]
        latlng = re.findall(r'parseFloat\((.+)\);', t)
        item['latlng'] = [latlng[0], latlng[1]]
        return item
        #response.xpath('//div[@class="property-address"]/text()').extract()[0].split(',')[2]
