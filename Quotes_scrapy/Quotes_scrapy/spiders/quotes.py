import scrapy 

class MySpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json'
        }
    

def parse(self, response):
    title = response.xpath('//h1/a/text()').get()
  
    citas = response.xpath("//span[@class = 'text' and @itemprop= 'text']/text()").getall()

    topTenTags = response.xpath('//div/span/a[@class="tag"]/text()').getall()
    yield {
            'titles': title,
            'quotes': citas,
            'top ten tags': topTenTags
        }

    next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
    
    if next_page_button_link:
        yield response.follow(next_page_button_link, callback=self.parse)
        """
        El metodo follow sigue el nuevo link, luego de que se hace la request   
        Este metodo posee un callback que ejecutara el metodo parse con el nuevo response
        """