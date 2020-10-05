# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    store = scrapy.Field()
    category = scrapy.Field()
    #categoryID = scrapy.Field()
    img = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()