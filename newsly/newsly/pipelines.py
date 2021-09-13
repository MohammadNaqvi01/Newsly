# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from app.models import TOI,TheHindu,HT

class TOIPipeline(object):
    def process_item(self, item, spider):
         print(spider.name)
         section=item['section']
         heading=item['heading']
         headline=item['headline']
         link=item['readmore']
         try:
            TOI.objects.create(
               section=section,heading=heading,headline=headline,link=link)
            print(item,"HURRAY SUCCESSFULLY SUBMITTED")
            return item
         except:
            print("Cant add Duplicate Fields")
            return item
class THPipeline(object):
    def process_item(self, item, spider):
         print(spider.name)
         section=item['section']
         heading=item['heading']
         headline=item['headline']
         link=item['readmore']
         try:
            TheHindu.objects.create(
               section=section,heading=heading,headline=headline,link=link)
            print(item,"HURRAY SUCCESSFULLY SUBMITTED")
            return item
         except:
            print("Cant add Duplicate Fields")
            return item
class HTPipeline(object):
    def process_item(self, item, spider):
         print(spider.name)
         section=item['section']
         heading=item['heading']
         headline=item['headline']
         link=item['readmore']
         try:
            HT.objects.create(
               section=section,heading=heading,headline=headline,link=link)
            print(item,"HURRAY SUCCESSFULLY SUBMITTED")
            return item
         except:
            print("Cant add Duplicate Fields")
            return item