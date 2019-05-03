# -*- coding: utf-8 -*-
import scrapy
from crawlerbot.items import TgItem
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from crawlerbot.district_names import district_map
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class threntSpider(scrapy.Spider):
    name = 'threntspider'
    output_name = 'thrent'

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
    try:
        with open(os.path.join(dirName, 'thlinkrent.json'), 'r') as f:
            data = json.load(f)
            urls = [d['link'] for d in data]
            # start_urls = urls
            start_urls = urls[:5000]
            # start_urls = ['https://www.thaihometown.com/home/1398887', 'https://www.thaihometown.com/condo/1475282', 'https://www.thaihometown.com/condo/1591028']
    except FileNotFoundError:
        pass

    def parse(self, response):
        item = TgItem()
        item['pid'] = response.request.url.split('/')[4]
        item['ptype'] = response.request.url.split('/')[3].capitalize()
        if item['ptype'] == 'Home':
            item['ptype'] = 'House'
        item['name'] = response.xpath('//div[@class="namedesw9"]/h1/text()').extract_first()
        rooms = response.xpath('//td[contains(text(),"จำนวนห้อง")]/../td[@class="table_set3"]/a/text()').extract()
        if len(rooms[0].split()) > 1:
            item['bed'] = rooms[0].split()[0]
        else:
            item['bed'] = rooms[0]
        item['bath'] = rooms[1].split()[0]
        district = response.xpath('//td[contains(text(),"เขตที่ตั้ง")]/../td[@class="table_set3"]/a/text()').extract_first()
        item['location'] = district_map[district]
        area = response.xpath('//div[@class="sqm_right"]/a/text()').extract_first().split()
        if area[1] == 'ตารางวา':
            item['size'] = float(area[0]) * 4
        else:
            item['size'] = float(area[0])
        price = response.xpath('//a[contains(text(),"ให้เช่า")]/text()').extract_first().split()
        item['price'] = price[1].replace(',','')
        item['daypost'] = response.xpath('//div[@class="datedetail"]/text()').extract_first()
        map_url = response.xpath('//iframe[@id="GMap"]/@src').extract_first()
        ggmap_url = response.xpath('//div[@class="maps_google2"]/a/@href').extract_first()
        if map_url:
            request = scrapy.Request(map_url, callback=self.parse_latlng)
            request.meta['item'] = item
            return request
        elif ggmap_url:
            browser = webdriver.Chrome()
            browser.get(ggmap_url)
            wait = WebDriverWait(browser, 30)
            # browser.find_element_by_xpath("//div[@id='pclose']").click()
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            # browser.implicitly_wait(30) # seconds
            browser.switch_to.frame(browser.find_element_by_xpath('//div[@id="divMapFull"]/iframe'))
            try:
                print("11111111 --------")
                nav1 = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"ดูแผนที่ขนาดใหญ่")]')))
                # nav1 = browser.find_element_by_xpath("//a[contains(text(),'ดูแผนที่ขนาดใหญ่')]")
                map_url = nav1.get_attribute('href')
                print(map_url + "   ---  11111111")
            except TimeoutException:
                print("22222222 --------")
                nav2 = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"View larger map")]')))
                # nav2 = browser.find_element_by_xpath("//a[contains(text(),'View larger map')]")
                map_url = nav2.get_attribute('href')
                print(map_url + "   ---  22222222")
            # nav = browser.find_element_by_xpath("//div[@class='google-maps-link']/a")
            # nav = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"ดูแผนที่ขนาดใหญ่")]')))
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
