from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawlerbot.spiders.thaihometown_crawl import ThaihometownCrawlSpider

process = CrawlerProcess(get_project_settings())
process.crawl(ThaihometownCrawlSpider)
process.start()
