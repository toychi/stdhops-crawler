# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import json
import os


class CrawlerbotPipeline(object):
    def process_item(self, item, spider):
        return item


class ThaihometownLinksPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')
        # Create directory
        dirName = 'Links/Thaihometown'

        try:
            # Create target Directory
            os.makedirs(dirName)
            print("Directory ", dirName, " Created ")
        except FileExistsError:
            print("Directory ", dirName, " already exists")

        self.file = open('Links/Thaihometown/thaihometown_links.json', 'w', encoding='utf8')
        self.file.write('[')
        # self.exporter = JsonLinesItemExporter(self.file)

    def close_spider(self, spider):
        print('Exporter closed')
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item
        
    


