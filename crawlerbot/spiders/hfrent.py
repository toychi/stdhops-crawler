import scrapy
from crawlerbot.items import TgItem
import json
import re
import os
from crawlerbot.district_names import districts, district_map
import datetime


class hfrentSpider(scrapy.Spider):
    name = 'hfrentspider'
    output_name = 'hfrent'
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlerbot.pipelines.JsonPipeline': 300,
            'crawlerbot.pipelines.MongoPipeline': 400
        }
        # 'LOG_FILE': 'crawlerbot/logs/demospider.log',
        # 'LOG_LEVEL': 'DEBUG'
    }

    curDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dirName = os.path.join(curDir, 'json')

    d_name = [d['name'] for d in districts]
    p = re.compile(".*(" + ('|'.join(d_name)) + ").*")

    try:
        with open(os.path.join(dirName, 'hflinkrent.json'), 'r') as f:
            data = json.load(f)
            urls = [d['link'] for d in data]
            # start_urls = urls
            start_urls = urls[500:]
    except FileNotFoundError:
        pass

    def parse(self, response):
        item = TgItem()
        item['pid'] = response.xpath('//div[@class="wrap clearfix"]/h4/text()').extract_first().split()[-1]
        item['name'] = response.xpath('//div[@class="propertyname"]/text()').extract_first().strip()
        address = response.xpath('//div[@class="property-address"]/text()').extract_first()
        if address is not None:
            m = hfrentSpider.p.search(address.title())
            item['location'] = m.group(1) if m is not None else ""
            if item['location'] in district_map.keys():
                item['location'] = district_map[item['location']]
        item['ptype'] = response.xpath('//div[@class="wrap clearfix"]/h5/span/small/text()').extract_first().split()[-1]
        item['size'] = response.xpath('//div[@class="property-meta clearfix"]/span/text()').extract_first().split()[0]
        # item['floor'] = response.xpath('//div[@class="box floors"]/span/text()').extract_first()
        posted_link = response.xpath('//ul[@class="slides"]/li/a/@href').extract_first()
        item['daypost'] = datetime.datetime.strptime(re.match('(\d+)\/(\d+)', posted_link), '%Y/%m')
        item['yearbuilt'] = response.xpath('//div[@class="box built"]/span/text()').extract_first()
        item['price'] = response.xpath('//div[@class="wrap clearfix"]/h5/span/text()').extract()[1].split()[0][1:].replace(',','')
        item['bed'] = response.xpath('//div[@class="property-meta clearfix"]/span/text()').extract()[1].split()[0]
        item['bath'] = response.xpath('//div[@class="property-meta clearfix"]/span/text()').extract()[2].split()[0]
        t = response.xpath('//div[@class="map-wrap clearfix"]/script').extract()[0]
        latlng = re.findall(r'parseFloat\((.+)\);', t)
        item['latlng'] = [latlng[0], latlng[1]]
        return item
        #response.xpath('//div[@class="property-address"]/text()').extract()[0].split(',')[2]
