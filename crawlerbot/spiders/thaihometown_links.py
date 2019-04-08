# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from crawlerbot.items import HouseLinkItem
import re


class ThaihometownLinksSpider(scrapy.Spider):
    name = 'thaihometown_links'
    file_name = 'thaihometown_links.json'
    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlerbot.pipelines.LinksPipeline': 400
        }
    }
    allowed_domains = ['thaihometown.com']
    start_urls = ['https://www.thaihometown.com/search/?page=2&Type=Home&Country=%A1%C3%D8%A7%E0%B7%BE%C1%CB%D2%B9%A4%C3&Submit=Search']

    BASE_URL = 'https://www.thaihometown.com/search/?page='
    APPEND_URL = '&Type=Home&Country=%A1%C3%D8%A7%E0%B7%BE%C1%CB%D2%B9%A4%C3&Submit=Search'

    def parse(self, response):
        last_page = response.xpath('//div[@id="PList"]/span/text()').extract_first().split('/')[1]
        for i in range(1, int(last_page)):
            absolute_url = self.BASE_URL + str(i) + self.APPEND_URL
            yield scrapy.Request(absolute_url, callback=self.parse_attr)

    def parse_attr(self, response):
        units = response.xpath('//div[@class="namedesw7"]/div[@onmouseover]')
        for h in units:
            item = HouseLinkItem()
            item['id'] = re.sub('[a-zA-Z]', '', h.xpath('@id').extract_first())
            item['name'] = h.xpath('a/text()').extract_first()
            item['link'] = h.xpath('a/@href').extract_first()
            item['maps'] = h.xpath('table/tr/td[@class="tablelist"]/a[contains(@href, "maps")]/@href').extract_first()
            yield item
