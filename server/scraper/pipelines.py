from scrapy.exceptions import DropItem
from index import db
from models import Blog


class EngineeringblogsPipeline(object):

    def process_item(self, item, spider):

        import pdb
        pdb.set_trace()
        return item
