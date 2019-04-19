from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawlerbot.spiders.tglinksale import tglinksaleSpider
from crawlerbot.spiders.tglinkrent import tglinkrentSpider
from crawlerbot.spiders.tgrent import tgrentSpider
from crawlerbot.spiders.tgsale import tgsaleSpider


process = CrawlerProcess(get_project_settings())

# Thaigerproperty Links
process.crawl(tglinksaleSpider)
process.crawl(tglinkrentSpider)

# # Thaigerproperty Properties
# process.crawl(thaigerrentSpider)
# process.crawl(thaigersaleSpider)
process.start()
