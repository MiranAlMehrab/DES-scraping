import scrapy

class DesSpider(scrapy.Spider):
    name = "des"

    start_urls = [
        'https://www.dse.com.bd/latest_share_price_scroll_l.php'
    ]

    def parse(self, response):
        requested_page = response.url.split("/")[-2]
        print("requested_page: "+requested_page)

        response_body = response.body
        print("response_body: ")
        print(response.body)


        
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')