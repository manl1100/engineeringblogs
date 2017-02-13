from scrapy.exceptions import DropItem


class EngineeringblogsPipeline(object):

    def process_item(self, item, spider):
        return item
