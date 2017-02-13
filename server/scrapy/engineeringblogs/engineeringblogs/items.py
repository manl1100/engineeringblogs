import scrapy


class EngineeringblogsItem(scrapy.Item):

    title = scrapy.Field()
    content = scrapy.Field()
