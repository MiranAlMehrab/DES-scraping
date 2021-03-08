import sys
import scrapy
from scrapy.loader import ItemLoader 
from DES_Scraping.items import CompanyItem

class DesSpider(scrapy.Spider):
    name = "companies"
    start_urls = ['https://www.dse.com.bd/company_listing.php']

    def parse(self, response):
        
        requested_page = response.url.split("/")[-2]
        main_div = response.xpath("//div[@class='col-md-12 col-sm-12 col-xs-18']/*")
    
        print('<------------------------------------------------------------- look here ------------------------------------------------------------->')
    
        for div in main_div[2].xpath("//div[@class='col-lg-4 col-md-4 col-sm-6 col-xs-12 background-white']"):
            category = div.xpath('./*')[0]
            category = category.xpath('./h2[@class="BodyHead"]/text()').get()

            items = []
            body_content = div.xpath('./*')[1]
            for company in body_content.xpath('./*'):
                item = company.xpath('text()').get()
                items.append(item.encode('ascii','ignore'))

            
            name_code_pairs = zip(items[0:][::2], items[1:][::2])
            for pair in name_code_pairs:
                item = CompanyItem()

                item['name'] = pair[1].strip('()')
                item['category'] = category
                item['trading_code'] = pair[0] 
                
                yield item


            # company_code = body_content.xpath('./*')[0]
            # company_full_name = body_content.xpath('./*')[1]

            # print(company_code.xpath('text()'))
            # company = company.xpath('text()').get()
            # company = company.encode('ascii','ignore')
            # print('one item: '+ company)

            # break
            
        print('<------------------------------------------------------------- look here ------------------------------------------------------------->')
        
        # for i in range(1, len(main_div)):    
            
        #     div_tds = None
        #     if i == 1: div_tds = first_div_of_table
        #     else: div_tds = main_div[i].xpath('./*')
            
        #     try:
        #         item = DESItem()

        #         item['name'] = (div_tds[1].xpath("text()").extract_first()).strip()
        #         item['last_traded_price'] = div_tds[2].xpath("text()").extract_first()
                
        #         yield item

        #     except:
        #         raise Exception("exception occurred")
        #         print("Oops!", sys.exc_info()[0], "occurred.")