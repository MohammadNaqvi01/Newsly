



from newsly.items import PersonItem
import scrapy

class NewsSpider(scrapy.Spider):


        name = 'news'
        start_urls = [
            'https://www.ndtv.com/',
        ]

        def parse(self, response):

                items=PersonItem()
        # for heading in response.css('.topnav_cont a'):
            #  yield {
                    # 'heading' : response.css(".topnav_cont a::text").getall() #heading.xpath('span/small/text()').get(),
            
            #  }


                for head in response.css(".topnav_cont a::text").getall():
                    
                    items['heading']=head
                    print(items['heading'])
                    yield items