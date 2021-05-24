# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class ScrapingItem(scrapy.Item):
    url = scrapy.Field()
    taxon = scrapy.Field()
    pict = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ScrapingItemLoader(ItemLoader):
    pass
