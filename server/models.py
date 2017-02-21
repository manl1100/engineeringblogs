from index import db


class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    company = db.Column(db.String(25))
    url = db.Column(db.String(300))
    thumbnail = db.Column(db.String(300))

    def __init__(self, title, company, url, thumbnail):
        self.title = title
        self.company = company
        self.url = url
        self.thumbnail = thumbnail

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'url': self.url,
            'thumbnail': self.thumbnail,
        }

    def __repr__(self):
        return '<Blog %r>' % (self.title)
