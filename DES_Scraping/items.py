# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags   

# item = DESItem()

# item['date'] = 
# item['trading_code']
# item['last_traded_price'] 
# item['high'] 
# item['low'] 
# item['opening_price'] 
# item['closing_price'] = 
# item['yesterdays_closing_price'] = 
# item['trade'] = 
# item['value_mn'] = 
# item['volume'] = 

# yield item

# input_processor = MapCompose(remove_tags),
# output_processor = TakeFirst()    

class DESItem(scrapy.Item):
    # date = scrapy.Field(
    #     input_processor = MapCompose(remove_tags),
    #     output_processor = TakeFirst()  
    # )
    
    trading_code = scrapy.Field()

    last_traded_price = scrapy.Field()
    
    high = scrapy.Field()
    
    low = scrapy.Field()
    
    # opening_price = scrapy.Field(
    #     input_processor = MapCompose(remove_tags),
    #     output_processor = TakeFirst()
    # )
    
    closing_price = scrapy.Field()
    
    yesterdays_closing_price = scrapy.Field()
    
    change = scrapy.Field()

    trade = scrapy.Field()
    
    value_mn = scrapy.Field()
    
    volume = scrapy.Field()