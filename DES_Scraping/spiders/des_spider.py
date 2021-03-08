import sys
import scrapy
from scrapy.loader import ItemLoader
from DES_Scraping.items import LatestItem

class DesSpider(scrapy.Spider):
    name = "latest"
    start_urls = ['https://www.dse.com.bd/latest_share_price_scroll_l.php']

    def parse(self, response):
        
        requested_page = response.url.split("/")[-2]
        table_rows = response.xpath("//table[@class = 'table table-bordered background-white shares-table fixedHeader']/*")
        first_row_of_table = response.xpath("//table[@class = 'table table-bordered background-white shares-table fixedHeader']/tbody/tr/*")
        
        for i in range(1, len(table_rows)):    
            
            row_tds = None
            if i == 1: row_tds = first_row_of_table
            else: row_tds = table_rows[i].xpath('./*')
            
            try:
                item = LatestItem()

                item['trading_code'] = (row_tds[1].xpath(".//a/text()").extract_first()).strip()
                item['last_traded_price'] = row_tds[2].xpath("text()").extract_first()
                item['high'] = row_tds[3].xpath("text()").extract_first()
                item['low'] = row_tds[4].xpath("text()").extract_first()
                item['closing_price'] = row_tds[5].xpath("text()").extract_first()
                item['yesterdays_closing_price'] = row_tds[6].xpath("text()").extract_first()
                item['change'] = row_tds[7].xpath("text()").extract_first()
                item['trade'] = row_tds[8].xpath("text()").extract_first()
                item['value_mn'] = row_tds[9].xpath("text()").extract_first()
                item['volume'] = row_tds[10].xpath("text()").extract_first()

                yield item

            except:
                raise Exception("exception occurred")
                print("Oops!", sys.exc_info()[0], "occurred.")
        
            
    def fetch_table_row_with_whitespaces():
        yield {
                "data": response.xpath("//tr").extract_first()
            }
