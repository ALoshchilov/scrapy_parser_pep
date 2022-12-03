import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('section#numerical-index td a::attr(href)')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title, *name = response.css('.page-title::text').get().split(' – ')
        yield PepParseItem({
            'number': title.replace('PEP ', ''),
            'name': ' - '.join(name),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get().strip()
        })
