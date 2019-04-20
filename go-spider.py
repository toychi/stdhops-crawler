from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawlerbot.spiders.tglinksale import tglinksaleSpider
from crawlerbot.spiders.tglinkrent import tglinkrentSpider
from crawlerbot.spiders.tgrent import tgrentSpider
from crawlerbot.spiders.tgsale import tgsaleSpider
from crawlerbot.spiders.hflinksale import hflinksaleSpider
from crawlerbot.spiders.hflinkrent import hflinkrentSpider


process = CrawlerProcess(get_project_settings())

# # Thaigerproperty Links
# process.crawl(tglinksaleSpider)
# process.crawl(tglinkrentSpider)

# # Thaigerproperty Properties
# process.crawl(tgrentSpider)
# process.crawl(tgsaleSpider)

# Homefinder Links
process.crawl(hflinkrentSpider)
process.crawl(hflinksaleSpider)

process.start()
