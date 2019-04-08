# -*- coding: utf-8 -*-
import scrapy
from crawlerbot.items import HouseItem
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ThaihometownCrawlSpider(scrapy.Spider):
    name = 'thaihometown_crawl'

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawlerbot.pipelines.MongoPipeline': 400
        }
        # 'LOG_FILE': 'crawlerbot/logs/demospider.log',
        # 'LOG_LEVEL': 'DEBUG'
    }

    with open('crawlerbot/links/thaihometown_links.json', 'r') as f:
        data = json.load(f)

    urls = [d['link'] for d in data]
    start_urls = urls[:10]
    # start_urls = ['https://www.thaihometown.com/home/516746']

    def parse(self, response):
        item = HouseItem()
        item['id'] = response.request.url.split('/')[4]
        item['name'] = response.xpath('//div[@class="namedesw9"]/h1/text()').extract_first()
        item['room'] = response.xpath(
            '//td[contains(text(),"จำนวนห้อง")]/../td[@class="table_set3"]/a/text()').extract()
        item['district'] = response.xpath('//td[contains(text(),"เขตที่ตั้ง")]/../td[@class="table_set3"]/a/text()').extract_first()
        item['area'] = response.xpath('//div[@class="sqm_right"]/a/text()').extract_first()
        item['price'] = response.xpath('//a[@class="linkprice"]/text()').extract_first()
        item['date'] = response.xpath('//div[@class="datedetail"]/text()').extract_first()

        map_url = response.xpath('//iframe[@id="GMap"]/@src').extract_first()
        ggmap_url = response.xpath('//div[@class="maps_google2"]/a/@href').extract_first()
        if map_url:
            request = scrapy.Request(map_url, callback=self.parse_latlng)
            request.meta['item'] = item
            return request
        elif ggmap_url:
            browser = webdriver.Chrome()
            browser.get(ggmap_url)
            wait = WebDriverWait(browser, 10)
            browser.switch_to.frame(browser.find_element_by_xpath('//div[@id="divMapFull"]/iframe'))
            # nav = browser.find_element_by_xpath("//div[@class='google-maps-link']/a")
            nav = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"View larger map")]')))
            map_url = nav.get_attribute('href')
            browser.close()
            try:
                item['latlng'] = re.search('=.+&z', map_url).group(0)[1:-2].split(',')
            except AttributeError:
                item['latlng'] = ','.split(',')
        else:
            item['latlng'] = ','.split(',')

        return item

    def parse_latlng(self, response):
        item = response.meta['item']
        text = response.xpath('//script[@type="text/javascript"]/text()').extract_first()
        try:
            item['latlng'] = re.search('\(.+\)', text).group(0)[1:-1].split(',')
        except AttributeError:
            item['latlng'] = ','.split(',')
        return item
