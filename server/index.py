from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import BaseConfig
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)
