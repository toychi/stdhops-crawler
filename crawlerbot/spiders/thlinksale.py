# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from crawlerbot.items import PropertyLinkItem
import re


class thlinksaleSpider(scrapy.Spider):
    name = 'thlinksalespider'
    output_name = 'thlinksale'
    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlerbot.pipelines.JsonPipeline': 300
        }
    }
    allowed_domains = ['thaihometown.com']
    start_urls = ['https://www.thaihometown.com/search/?page=2&Type=Home&Country=%A1%C3%D8%A7%E0%B7%BE%C1%CB%D2%B9%A4%C3&Submit=Search']

    BASE_URL = 'https://www.thaihometown.com/search/?page='
    APPEND_URL_1 = '&Type=Home&FormType=Sale&Country=%A1%C3%D8%A7%E0%B7%BE%C1%CB%D2%B9%A4%C3&Submit=Search'
    APPEND_URL_2 = '&Type=Condominiem&FormType=Sale&Country=%A1%C3%D8%A7%E0%B7%BE%C1%CB%D2%B9%A4%C3&Submit=Search'

    def parse(self, response):
        # last_page = response.xpath('//div[@id="PList"]/span/text()').extract_first().split('/')[1]
        # for i in range(1, int(last_page)):
        for i in range(1, 100):
            absolute_url = self.BASE_URL + str(i) + self.APPEND_URL_1
            yield scrapy.Request(absolute_url, callback=self.parse_attr)
        for i in range(1, 100):
            absolute_url = self.BASE_URL + str(i) + self.APPEND_URL_2
            yield scrapy.Request(absolute_url, callback=self.parse_attr)

    def parse_attr(self, response):
        units = response.xpath('//div[@class="namedesw7"]/div[@onmouseover]')
        for h in units:
            item = PropertyLinkItem()
            item['pid'] = re.sub('[a-zA-Z]', '', h.xpath('@id').extract_first())
            item['name'] = h.xpath('a/text()').extract_first()
            item['link'] = h.xpath('a/@href').extract_first()
            item['maps'] = h.xpath('table/tr/td[@class="tablelist"]/a[contains(@href, "maps")]/@href').extract_first()
            yield item
