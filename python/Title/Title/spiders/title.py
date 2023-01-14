import scrapy


class TitleSpider(scrapy.Spider):
    name = 'title'
    allowed_domains = ['c.biancheng.net']
    start_urls = ['http://c.biancheng.net/']

    def parse(self, response):
        pass
