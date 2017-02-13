import scrapy
from scrapy.selector import Selector
from ..items import EngineeringblogsItem

URL_PATTERN = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


class UberSpider(scrapy.Spider):
    name = 'uber'

    start_urls = [
        'https://eng.uber.com/',
    ]

    def parse(self, response):
        posts = response.css('.post')
        for post in posts:
            thumbnail = response.css(
                '.featured-image::attr(style)').re_first(URL_PATTERN)
            title = post.css('.post_link a::text').extract()
            url = post.css('.post_link a::attr(href)').extract()
            yield EngineeringblogsItem(company=self.name,
                                       title=title,
                                       url=url,
                                       thumbnail=thumbnail)
