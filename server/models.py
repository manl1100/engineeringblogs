from index import db


class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(25))
    title = db.Column(db.String(100))
    url = db.Column(db.String(300))
    thumbnail = db.Column(db.String(300))

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
