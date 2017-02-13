import scrapy
from scrapy.selector import Selector
from ..items import EngineeringblogsItem


class BlogSpider(scrapy.Spider):
    name = 'blogs'

    start_urls = [
        'https://eng.uber.com/',
    ]

    def parse(self, response):
        post = response.css('.post')
        if post is not None:
            title = post.css('.post-title::text').extract()
            content = post.css('.post-content p span::text').extract()
            yield EngineeringblogsItem(title=title, content=content)

        links = response.css('.post_link a::attr(href)').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse)
