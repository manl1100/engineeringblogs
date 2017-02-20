from scrapy.exceptions import DropItem
from index import db
from models import Blog


class EngineeringblogsPipeline(object):

    def process_item(self, item, spider):
        blog = Blog(item['title'], item['company'],
                    item['url'], item['thumbnail'])
        db.session.add(blog)
        db.session.commit()
        return item
