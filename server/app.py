from index import app, db, api
from flask import Flask, jsonify, request
from flask_restful import Resource, reqparse
from models import Blog

parser = reqparse.RequestParser()
parser.add_argument('title')


class EngineeringBlog(Resource):

    def get(self):
        blogs = Blog.query.all()
        return jsonify({'blogs': [blog.to_dict() for blog in blogs]})

    def post(self):
        args = parser.parse_args()
        blog = Blog(args['title'])
        db.session.add(blog)
        db.session.commit()
        return 1, 201


api.add_resource(EngineeringBlog, '/blogs')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
