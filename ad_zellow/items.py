# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdZellowItem(scrapy.Item):
    id = scrapy.Field()
    image_src = scrapy.Field()
    detail_url = scrapy.Field()
    status_type = scrapy.Field()
    status_text = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
