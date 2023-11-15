import scrapy
from scrapy.http import Request


class HockeyteamsSpider(scrapy.Spider):
    name = "hockeyteams"
    start_urls = ["https://www.scrapethissite.com/pages/forms/?page_num={page}"]
    n_pages = 24

    def start_requests(self):
        for page in range(1, self.n_pages + 1):
            yield Request(url=self.start_urls[0].format(page=page), callback=self.parse)

    def parse(self, response):
        columns = response.xpath('//tr[@class="team"]')

        for column in columns:
            team = column.xpath('./td/text()').get()
            year = column.xpath('./td[@class="year"]/text()').get()
            wins = column.xpath('./td[@class="wins"]/text()').get()
            losses = column.xpath('./td[@class="losses"]/text()').get()
            ot_losses = column.xpath('./td[@class="ot-losses"]/text()').get()
            win_pct = column.xpath('./td[@class="pct text-success" or @class="pct text-danger"]/text()').get()
            goals_for = column.xpath('./td[@class="gf"]/text()').get()
            goals_against = column.xpath('./td[@class="ga"]/text()').get()
            diff = column.xpath('./td[@class="diff text-success" or @class="diff text-danger"]/text()').get()
            
            if float(self.clean_text(win_pct)) >= 0.5:
                win_category = 'success'
            else:
                win_category = 'danger'

            yield {'team': self.clean_text(team), 'year': year, 'wins': wins, 'losses': losses, 'ot_losses': ot_losses,
                  'win_pct': win_pct, 'win_category': win_category, 'goals_for': goals_for, 'goals_against': goals_against,
                  'diff': diff}
            
    def clean_text(self, raw_text):
        return raw_text.strip('\n').strip()
    


        
