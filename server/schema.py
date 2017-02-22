from models import Blog
from index import ma


class BlogSchema(ma.ModelSchema):

    class Meta:
        model = Blog


blogs_schema = BlogSchema()
