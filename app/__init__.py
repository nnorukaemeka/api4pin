import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_uuid import FlaskUUID
from flask_restful import Resource, Api
import uuid
from hashFunc import HashTable, GetKeyValue
# from flask_pymongo import PyMongo

# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


# Initialize Flask Sql Alchemy
db = SQLAlchemy(app)

# Initialize Flask Api
api = Api(app)

# # Initialize Flask PyMongo
# mongo = PyMongo(app)

# Import the application views
from app import views

