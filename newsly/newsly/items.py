# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from app.models import TheHindu,HT,TOI

class THItem(DjangoItem):
    django_model = TheHindu

class HTItem(DjangoItem):
    django_model = HT

class TOIItem(DjangoItem):
    django_model = TOI






# class TheHinduItem(scrapy.Item):
#     # define the fields for your item here like:
#      section = scrapy.Field()
#      heading = scrapy.Field()
#      headline = scrapy.Field()
#      readmore = scrapy.Field()

# class TOIItem(scrapy.Item):
#     # define the fields for your item here like:
#      section = scrapy.Field()
#      heading = scrapy.Field()
#      headline = scrapy.Field()
#      readmore = scrapy.Field()


# class HTItem(scrapy.Item):
#     # define the fields for your item here like:
#      section = scrapy.Field()
#      heading = scrapy.Field()
#      headline = scrapy.Field()
#      readmore = scrapy.Field()
