import scrapy
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser
from ..items import AdZellowItem
import json

class ZellowSpider(scrapy.Spider):
    name = 'zellow'
    allowed_domains = ['www.zillow.com']
    
    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            cookies=cookie_parser()
        )

    def parse(self, response):
        json_resp = json.loads(response.body)
        houses = json_resp.get('searchResults').get('listResults')
        for house in houses:
            loader = ItemLoader(item=AdZellowItem())
            loader.add_value('id', house.get('id'))
            loader.add_value('image_urls', house.get('imgSrc'))
            loader.add_value('detail_url', house.get('detailUrl'))
            loader.add_value('status_type', house.get('statusType'))
            loader.add_value('status_text', house.get('statusText'))
            loader.add_value('price', house.get('price'))
            loader.add_value('address', house.get('address'))
            yield loader.load_item()
