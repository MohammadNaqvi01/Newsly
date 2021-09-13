from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())#to get setting instance

#passing 
process.crawl('ht')
process.crawl('th')
process.crawl('toi')

process.start()  # the script will block here until the crawling is finished