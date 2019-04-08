from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawlerbot.spiders.thaigerlinksale import thaigerlinksaleSpider

process = CrawlerProcess(get_project_settings())
process.crawl(thaigerlinksaleSpider)
process.start()
