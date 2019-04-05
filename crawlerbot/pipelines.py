# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import json
import codecs


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


class HflinkrentPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('hflinkrent.json', 'a')
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


class HflinksalePipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('hflinksale.json', 'a')
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


class TgrentPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('C:/Users/Administrator/Desktop/Senior/GitCrawl/stdhops-crawler/crawlerbot/spiders/tgrent.json', 'w', encoding='utf8')
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

		
class TgsalePipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('C:/Users/Administrator/Desktop/Senior/GitCrawl/stdhops-crawler/crawlerbot/spiders/tgsale.json', 'w', encoding='utf8')
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


class HfrentPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('C:/Users/Administrator/Desktop/Senior/GitCrawl/stdhops-crawler/crawlerbot/spiders/hfrent.json', 'w', encoding='utf8')
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

class HfsalePipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('C:/Users/Administrator/Desktop/Senior/GitCrawl/stdhops-crawler/crawlerbot/spiders/hfsale.json', 'w', encoding='utf8')
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

class TglinksalePipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('tglinksale.json', 'a')
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

class TglinkrentPipeline(object):
    def open_spider(self, spider):
        print('Exporter opened')

        self.file = open('tglinkrent.json', 'w')
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