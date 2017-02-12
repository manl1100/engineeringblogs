from index import db


class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    def __init__(self, title):
        self.title = title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
        }

    def __repr__(self):
        return '<Blog %r>' % (self.title)

db.create_all()
