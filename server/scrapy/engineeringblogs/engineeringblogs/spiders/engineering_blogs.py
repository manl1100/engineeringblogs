import scrapy
from scrapy.selector import Selector
from ..items import EngineeringblogsItem


class BlogSpider(scrapy.Spider):
    name = 'blogs'

    start_urls = [
        'https://eng.uber.com/',
    ]

    def parse(self, response):

        sel = Selector(response)

        titles = sel.css('.post_link').xpath('./a/text()').extract()
        print titles
        return [EngineeringblogsItem(title=title) for title in titles]
