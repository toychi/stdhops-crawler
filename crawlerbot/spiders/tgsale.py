import scrapy
from crawlerbot.items import TgItem
import json
import re


class thaigersaleSpider(scrapy.Spider):
    name = 'tgsalespider'
    output_name = 'tgsale'

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlerbot.pipelines.JsonPipeline': 300,
            'crawlerbot.pipelines.MongoPipeline': 400
        }
        # 'LOG_FILE': 'crawlerbot/logs/demospider.log',
        # 'LOG_LEVEL': 'DEBUG'
    }

    with open('crawlerbot/json/tglinksale.json', 'r') as f:
        data = json.load(f)
        urls = [d['link'] for d in data]
        start_urls = urls

    def parse(self, response):
        item = TgItem()
        item['pid'] = response.xpath('//div[@class="unit_id"]/strong/text()').extract_first()
        item['name'] = response.xpath('//h2[@class="project_title"]/a/text()').extract_first()
        item['location'] = response.xpath('//ul[@class="basic-list"]/li/strong/text()').extract()[1].split(',')[0].strip()
        item['ptype'] = response.xpath('//ul[@class="basic-list"]/li/strong/text()').extract()[0]
        item['size'] = response.xpath('//div[@class="txt"]/strong/text()').extract()[2].split()[0]
        if item['ptype'] == 'Condo':
            item['floor'] = response.xpath('//ul[@class="property-list"]/li/img[contains(@class,"floor_logo")]/../div/text()').extract_first()
        else:
            item['floor'] = response.xpath('//ul[@class="basic-list"]/li/span[contains(text()," Number of Floors in Building:")]/../strong/text()').extract_first()
        complete_year = response.xpath('//ul[@class="basic-list"]/li/strong[contains(text(),"Completed")]/text()').extract_first().split()
        item['yearbuilt'] = complete_year[1][1:] + ' ' +complete_year[2][:-1]
        item['price'] = response.xpath('//span[@class="unit_price"]/text()').extract_first()[1:]
        if item['price'] is not None:
            item['price'] = item['price'].replace(',','')
        item['bed'] = response.xpath('//div[@class="txt"]/strong/text()').extract_first()
        item['bath'] = response.xpath('//div[@class="txt"]/strong/text()').extract()[1]
        item['furniture'] = response.xpath('//ul[@class="basic-list"]/li/strong[contains(text(),"Furnished")]/text()').extract_first().strip()
        item['daypost'] = response.xpath('//li[@class="hidden-sm hidden-xs"]/text()').extract_first().split()[0]
        # Map
        map_url = "https://property.thethaiger.com/get-map/unit/" + item['pid']
        request = scrapy.Request(map_url, callback=self.parse_latlng)
        request.meta['item'] = item
        return request
        
    def parse_latlng(self, response):
        item = response.meta['item']
        lat = response.xpath('//input[@class="centerLat"]/@value').extract_first()
        lng = response.xpath('//input[@class="centerLng"]/@value').extract_first()
        item['latlng'] = [lat, lng]
        return item
