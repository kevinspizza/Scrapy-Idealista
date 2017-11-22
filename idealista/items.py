# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IdealistaItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    rooms = scrapy.Field()
    m2 = scrapy.Field()
    description = scrapy.Field()
    costs_per_month = scrapy.Field()
    address = scrapy.Field()
    addons = scrapy.Field()


class SellItem(IdealistaItem):
    drop_price = scrapy.Field()
    price_per_m2 = scrapy.Field()


class RentItem(IdealistaItem):
    rent = scrapy.Field()
