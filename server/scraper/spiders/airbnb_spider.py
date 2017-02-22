import scrapy
from scrapy.selector import Selector
from ..items import EngineeringblogsItem


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'

    start_urls = [
        'http://nerds.airbnb.com/'
    ]

    def parse(self, response):
        posts = response.css('.post')
        for post in posts:
            thumbnail = post.css('img::attr(src)').extract_first()
            title = post.css('h3 strong::text').extract_first()
            url = post.css('.a::attr(href)').extract_first()
            yield EngineeringblogsItem(company=self.name,
                                       title=title,
                                       url=url,
                                       thumbnail=thumbnail)
