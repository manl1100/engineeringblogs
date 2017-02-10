from index import db
import datetime


class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
