import scrapy 

class MySpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
  
        citas = response.xpath("//span[@class = 'text' and @itemprop= 'text']/text()").getall()

        topTenTags = response.xpath('//div/span/a[@class="tag"]/text()').getall()
        yield {
            'titles': title,
            'quotes': citas,
            'top ten tags': topTenTags
        }

        print('\n\n\n')
        print(title)