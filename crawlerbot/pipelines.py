# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import json
import re
import os
import pymongo


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

        self.json_list = []
        # self.file.write('[')

    def close_spider(self, spider):
        with open('Links/Thaihometown/thaihometown_links.json', 'w', encoding='utf8') as file:
            file.write(json.dumps(self.json_list, indent=0, separators=(',', ':'), ensure_ascii=False))
        print('Exporter closed')

    def process_item(self, item, spider):
        self.json_list.append(dict(item))
        return item


class MongoPipeline(object):

    def __init__(self):
        self.mongo_uri = 'mongodb://127.0.0.1:27017'
        self.mongo_db = 'stdhops'
        self.collection_name = 'house'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        print("Connected to MongoDB")

    def close_spider(self, spider):
        self.client.close()
        print("Connection is closed")

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
