import scrapy

from doubantop250.items import Doubantop250Item


class DoubantopSpider(scrapy.Spider):
    name = 'doubantop'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    start=0

    def parse(self, response):
        dd_list = response.xpath('//ol[@class="grid_view"]/li')
        item = Doubantop250Item()
        for dd in dd_list:
            item['name']=dd.xpath('.//div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()').get().strip()
            item['star']=dd.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').get().strip()
            yield item
        if self.start < 225:  # 判断条件
            self.start +=25
            url = 'https://movie.douban.com/top250?start='+str(self.start)+'&filter='
            # 把url交给secheduer入队列
            # response会自动传给 callback 回调的 parse()函数 
            #Scrapy.request()向url发起请求，并将响应结果交给回调的解析函数
            yield scrapy.Request(url=url, callback=self.parse)  

