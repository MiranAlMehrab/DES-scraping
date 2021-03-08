import scrapy

class LatestItem(scrapy.Item):
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



class CompanyItem(scrapy.Item): 
    name = scrapy.Field()
    category = scrapy.Field()
    trading_code = scrapy.Field()


class DisplayCompanyItem(scrapy.Item): 
    name = scrapy.Field()
    sector = scrapy.Field()
    category = scrapy.Field()
    total_no_of_outstanding_securities = scrapy.Field()
