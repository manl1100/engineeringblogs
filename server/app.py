from index import api, app, db
from flask import Flask, jsonify
from flask_restful import Resource, reqparse
from models import Blog
from schema import blogs_schema


class EngineeringBlog(Resource):

    def get(self):
        blogs = Blog.query.all()
        return blogs_schema.dump(blogs, many=True).data


api.add_resource(EngineeringBlog, '/blogs')
