



from newsly.items import TOIItem
import scrapy

class NewsSpider(scrapy.Spider):


        name = 'toi'
        start_urls = [
            'https://timesofindia.indiatimes.com/news'
            
        ]
        
        custom_settings={
                'ITEM_PIPELINES':{
                        
                        'newsly.pipelines.TOIPipeline': 1,
                        # 'newsly.pipelines.TOIImagesPipeline': 1
                }
        }
        
        def parse(self, response):

                items=TOIItem()
        # for heading in response.css('.topnav_cont a'):
            #  yield {
                    # 'heading' : response.css(".topnav_cont a::text").getall() #heading.xpath('span/small/text()').get(),
            
            #  }
            #                 
                link=response.url
                items['section']='Latest'

                
                heading=response.css(".w_tle a::text").getall()

                items['heading']=heading
                print(heading)
                
                headline=response.css(".w_desc::text").getall()
                items['headline']=headline
                print(headline)
                
                links=response.css(".w_tle a::attr(href)").getall()
                
                for i in links:
                  link=str(link)+i      
                  items['readmore']=link
                print(link)

                yield items
