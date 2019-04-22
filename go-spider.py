from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawlerbot.spiders.tglinksale import tglinksaleSpider
from crawlerbot.spiders.tglinkrent import tglinkrentSpider
from crawlerbot.spiders.tgrent import tgrentSpider
from crawlerbot.spiders.tgsale import tgsaleSpider
from crawlerbot.spiders.hflinksale import hflinksaleSpider
from crawlerbot.spiders.hflinkrent import hflinkrentSpider
from crawlerbot.spiders.hfrent import hfrentSpider
from crawlerbot.spiders.hfsale import hfsaleSpider
from crawlerbot.spiders.thlinksale import thlinksaleSpider
from crawlerbot.spiders.thlinkrent import thlinkrentSpider
from crawlerbot.spiders.thsale import thsaleSpider
from crawlerbot.spiders.thrent import threntSpider


process = CrawlerProcess(get_project_settings())

# # Thaigerproperty Links
# process.crawl(tglinksaleSpider)
# process.crawl(tglinkrentSpider)

# # Thaigerproperty Properties
# process.crawl(tgrentSpider)
# process.crawl(tgsaleSpider)

# # Homefinder Links
# process.crawl(hflinkrentSpider)
# process.crawl(hflinksaleSpider)

# # Homefinder Properties
# process.crawl(hfrentSpider)
# process.crawl(hfsaleSpider)

# # Thaihometown Links
# process.crawl(thlinksaleSpider)
# process.crawl(thlinkrentSpider)

# Thaihometown Properties
process.crawl(thsaleSpider)
process.crawl(threntSpider)

process.start()
