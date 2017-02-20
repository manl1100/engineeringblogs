import scrapy
from scrapy.selector import Selector
from ..items import EngineeringblogsItem

URL_PATTERN = 'http[s]?.*\.(?:png|jpg)'


class UberSpider(scrapy.Spider):
    name = 'uber'

    start_urls = [
        'https://eng.uber.com/',
    ]

    def parse(self, response):
        posts = response.css('.post')
        for post in posts:
            thumbnail = post.css(
                '.featured-image::attr(style)').re_first(URL_PATTERN)
            title = post.css('.post_link a::text').extract_first()
            url = post.css('.post_link a::attr(href)').extract_first()
            yield EngineeringblogsItem(company=self.name,
                                       title=title,
                                       url=url,
                                       thumbnail=thumbnail)
