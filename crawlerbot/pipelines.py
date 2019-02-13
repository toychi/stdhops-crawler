# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import json


class CrawlerbotPipeline(object):
    def process_item(self, item, spider):
        return item


class ThaihometownPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('thaihometown.json', 'w')
        self.file.write('[')
        # self.exporter = JsonLinesItemExporter(self.file)

    def close_spider(self, spider):
        print('Exporter closed')
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item
		
		
class HomefinderPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('homefinder.json', 'a')
        self.file.write('[')
        # self.exporter = JsonLinesItemExporter(self.file)

    def close_spider(self, spider):
        print('Exporter closed')
        self.file.write(']')
        self.file.close()
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item

class ThaigerPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('thaiger.json', 'a')
        self.file.write('[')
        # self.exporter = JsonLinesItemExporter(self.file)

    def close_spider(self, spider):
        print('Exporter closed')
        self.file.write(']')
        self.file.close()
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item

class ThaisrcPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('bkkaccident.json', 'a')
        self.file.write('[')
        # self.exporter = JsonLinesItemExporter(self.file)

    def close_spider(self, spider):
        print('Exporter closed')
        self.file.write(']')
        self.file.close()
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item
	
class aqiPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('aqi.json', 'a')
        self.file.write('[')
        # self.exporter = JsonLinesItemExporter(self.file)

    def close_spider(self, spider):
        print('Exporter closed')
        self.file.write(']')
        self.file.close()
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item