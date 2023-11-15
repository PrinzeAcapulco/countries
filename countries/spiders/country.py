import scrapy


class CountrySpider(scrapy.Spider):
    name = "country"
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        boxes = response.xpath('//div[@class="col-md-4 country"]')

        for box in boxes:
            country = box.xpath('./h3/text()[2]').get()
            capital = box.xpath('.//span[@class="country-capital"]/text()').get()
            population = box.xpath('.//span[@class="country-population"]/text()').get()
            area = box.xpath('.//span[@class="country-area"]/text()').get()

            yield {'country': self.clean_country(country), 'capital': capital, 'population': population, 'area': area}

    def clean_country(self, raw_country):
        return raw_country.strip('\n').strip()
            

    
