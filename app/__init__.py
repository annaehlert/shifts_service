from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import app


application = Flask(__name__)

# API
api = Api(application)

# SQLAlchemy
db = SQLAlchemy(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(application)

# marshmallow
ma = Marshmallow(application)

from app import views