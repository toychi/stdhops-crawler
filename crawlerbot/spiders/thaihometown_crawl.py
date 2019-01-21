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
    start_urls = ['https://www.thaihometown.com/home/516746']

    def parse(self, response):
        item = HouseItem()
        item['id'] = response.request.url.split('/')[4]
        item['name'] = response.xpath('//div[@class="namedesw9"]/h1/text()').extract_first()
        item['room'] = response.xpath(
            '//td[contains(text(),"จำนวนห้อง")]/../td[@class="table_set3"]/a/text()').extract()
        item['area'] = response.xpath('//div[@class="sqm_right"]/a/text()').extract_first()
        item['price'] = response.xpath('//a[@class="linkprice"]/text()').extract_first()
        map_url = response.xpath('//iframe[@id="GMap"]/@src').extract_first()
        ggmap_url = response.xpath('//div[@class="maps_google2"]/a/@href').extract_first()
        if map_url:
            latlng = scrapy.Request(map_url, callback=self.parse_latlng)
        elif ggmap_url:
            browser = webdriver.Chrome()
            browser.get(ggmap_url)
            wait = WebDriverWait(browser, 10)
            browser.switch_to.frame(browser.find_element_by_xpath("//div[@id='divMapFull']/iframe"))
            # nav = browser.find_element_by_xpath("//div[@class='google-maps-link']/a")
            nav = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='google-maps-link']/a")))
            map_url = nav.get_attribute('href')
            browser.close()
            try:
                latlng = re.search('=.+&z', map_url).group(0)[1:-2]
            except AttributeError:
                latlng = ','
        else:
            latlng = ','
        item['latlng'] = latlng.split(',')

        with open('house.json', 'w', encoding='utf8') as f:
            json.dump(dict(item), f, ensure_ascii=False)

        # with open('house2.json', 'w') as d:
        #     line = json.dumps(dict(item)) + ",\n"
        #     d.write(line)

        pass

    def parse_latlng(self, response):
        text = response.xpath('//script[@type="text/javascript"]/text()').extract_first()
        try:
            latlng = re.search('\(.+\)', text).group(0)[1:-1]
        except AttributeError:
            latlng = ','
        return latlng
