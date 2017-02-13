import scrapy


class EngineeringblogsItem(scrapy.Item):

    company = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    thumbnail = scrapy.Field()
    url = scrapy.Field()
