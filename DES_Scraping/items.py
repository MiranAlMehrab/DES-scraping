import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags   

class DESItem(scrapy.Item):

    # date = scrapy.Field()
    trading_code = scrapy.Field()
    last_traded_price = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    # opening_price = scrapy.Field()
    closing_price = scrapy.Field()
    yesterdays_closing_price = scrapy.Field()
    change = scrapy.Field()
    trade = scrapy.Field()
    value_mn = scrapy.Field()
    volume = scrapy.Field()