# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from app.models import Person

# class NewslyItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

from scrapy_djangoitem import DjangoItem

class PersonItem(DjangoItem):
    django_model = Person