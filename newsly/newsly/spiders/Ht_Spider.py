



from newsly.items import HTItem
import scrapy

class NewsSpider(scrapy.Spider):


        name = 'ht'
        url='httpd://www.'
        start_urls = [
            'https://www.hindustantimes.com/latest-news'
        ]
        
        custom_settings={
                'ITEM_PIPELINES':{
                        
                        'newsly.pipelines.HTPipeline': 1,
                       # 'newsly.pipelines.HTImagesPipeline': 1
                }
        }
        def parse(self, response):

                items=HTItem()
        # for heading in response.css('.topnav_cont a'):
            #  yield {
                    # 'heading' : response.css(".topnav_cont a::text").getall() #heading.xpath('span/small/text()').get(),
            
            #  }                
                
                
                items['section']="Latest News"
        
                heading=response.css(".hdg3 a::text").getall()
                items['heading']=heading
                print(heading)
                headline=response.css("").getall()
                items['headline']=headline
                print(headline)

                links=response.css(".hdg3 a::attr(href)").getall()
                
                

                items['readmore']=links
                print(links)
                
                yield items

