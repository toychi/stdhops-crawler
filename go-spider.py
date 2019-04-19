from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawlerbot.spiders.thaigerlinksale import thaigerlinksaleSpider
from crawlerbot.spiders.tgrent import thaigerrentSpider
from crawlerbot.spiders.tgsale import thaigersaleSpider


process = CrawlerProcess(get_project_settings())
# process.crawl(thaigerlinksaleSpider)
process.crawl(thaigerrentSpider)
process.crawl(thaigersaleSpider)
process.start()
