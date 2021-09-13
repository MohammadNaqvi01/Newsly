




from newsly.items import THItem
import scrapy

class NewsSpider(scrapy.Spider):

        count=0
        name = 'th'
        start_urls = [
            'https://www.thehindu.com/latest-news/'
            
        ]
        items=THItem()
        items['section']='Latest News'
        items['readmore']="read"
        custom_settings={
                'ITEM_PIPELINES':{'newsly.pipelines.THPipeline': 1,
                #'newsly.pipelines.THImagesPipeline': 1
               
                }
        }
        def parse(self, response):
                
              
                follow=response.css(".latest-news li a::attr(href)").getall()    
                  
               
                for i in follow:
                 
                  yield response.follow(i,self.parse_news)
                 
             # for heading in response.css('.topnav_cont a'):
            #  yield {
                    # 'heading' : response.css(".topnav_cont a::text").getall() #heading.xpath('span/small/text()').get(),
            
            #  }  
                

        def parse_news(self,response):
                self.items['readmore']=response.request.url
                print(response.request.url)
                def extract_with_css(query):
                        return response.css(query).get(default='').strip()                
                heading=extract_with_css("h1.title::text")
                self.items['heading']=heading
                print(heading)
                        
                headline=extract_with_css("h2.intro::text")
                self.items['headline']=headline
                print(headline)
                
           
         
                
                yield self.items 
                

                