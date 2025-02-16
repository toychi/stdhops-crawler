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
import codecs
import datetime


class CrawlerbotPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

    def __init__(self):
        self.mongo_uri = 'mongodb://127.0.0.1:27017'
        self.mongo_db = 'spatioreps'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection_name = spider.output_name
        print("Connected to MongoDB")

    def close_spider(self, spider):
        self.client.close()
        print("Connection is closed")

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item


class JsonPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')
        # Create directory
        curDir = os.path.dirname(os.path.abspath(__file__))
        dirName = os.path.join(curDir, 'json')
        try:
            # Create target Directory
            os.makedirs(dirName)
            print("Directory ", dirName, " created ")
        except FileExistsError:
            print("Directory ", dirName, " already exists")

        self.json_list = []
        self.file_name = os.path.join(dirName, spider.output_name + '.json')

    def close_spider(self, spider):
        with open(self.file_name, 'w', encoding='utf8') as outfile:
            json.dump(self.json_list, outfile, default = self.myconverter)
        print('Exporter closed')
        
    def process_item(self, item, spider):
        self.json_list.append(dict(item))
        return item

    def myconverter(_, o):
        if isinstance(o, datetime.datetime):
            return o.__str__()
