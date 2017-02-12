from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
api = Api(app)
