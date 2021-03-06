import sys
import scrapy
from DES_Scraping.items import DESItem
from scrapy.loader import ItemLoader 



class DesSpider(scrapy.Spider):
    name = "des"

    start_urls = [
        'https://www.dse.com.bd/latest_share_price_scroll_l.php'
    ]

    def parse(self, response):
        
        requested_page = response.url.split("/")[-2]

        # print('debug point: ------------------------')
        # print(response.xpath("/html/body/div[2]/section/div/div[3]/div[1]/div[2]/div[1]/div[1]/table/tbody[1]/tr.[*/2]"))
        
        # table = response.xpath(".//table[@class = 'table table-bordered background-white shares-table fixedHeader']/*")
        # print('-----------------len-----------------')
        # print(len(table))

        # tbody_counter = 0
        # for tbody in table:
            
        #     tbody_counter += 1
        




        trs = response.xpath("//table[@class = 'table table-bordered background-white shares-table fixedHeader']/*")
        
        for i in range(2, len(trs)):

            print('----------------------------------- look here -----------------------------------: '+str(i))
            print(trs[i].xpath('./*'))
            
            # if i == 1:
            #     list_td = trs[i].xpath('./*') 
            #     print(len(trs[i].xpath('./*')))
            
             
            list_td = trs[i].xpath('./*')
            print(len(trs[i].xpath('./*')))

            try:
                item = DESItem()

                item['trading_code'] = (list_td[1].xpath(".//a/text()").extract_first()).strip()
                item['last_traded_price'] = list_td[2].xpath("text()").extract_first()
                item['high'] = list_td[3].xpath("text()").extract_first()
                item['low'] = list_td[4].xpath("text()").extract_first()
                # item['opening_price'] = 
                item['closing_price'] = list_td[5].xpath("text()").extract_first()
                item['yesterdays_closing_price'] = list_td[6].xpath("text()").extract_first()
                item['change'] = list_td[7].xpath("text()").extract_first()
                item['trade'] = list_td[8].xpath("text()").extract_first()
                item['value_mn'] = list_td[9].xpath("text()").extract_first()
                item['volume'] = list_td[10].xpath("text()").extract_first()

                yield item

            except:
                print('exception khaise')
                raise Exception("exception khaise")
                print("Oops!", sys.exc_info()[0], "occurred.")
        
            # yield {
            #     "data": response.xpath("//tr").extract_first()
            # }
