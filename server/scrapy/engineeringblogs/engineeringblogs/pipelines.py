from scrapy.exceptions import DropItem


class EngineeringblogsPipeline(object):

    def process_item(self, item, spider):
        if not item['title'] or not item['content']:
            raise DropItem
        return item
