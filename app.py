import os
import uuid

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config["MONGO_DBNAME"] = "skydivereviews"
# app.config["MONGO_URI"] = "mongodb://localhost:27017/skydivereviews"
app.config["MONGO_URI"] = "mongodb://admin:password1@ds155192.mlab.com:55192/skydivereviews"
mongo = PyMongo(app)

CORS(app)


@app.route("/")
def home():
    return "Home route"


@app.route("/addinstructor")
def addInstructor():
    return "add instructor route"


@app.route("/login")
def login():
    return "login page"


# @app.route("/add")
# def add():
#     instructor = mongo.db.instructors
#     instructor.insert({'firstName': 'Ballsack'})
#     return 'added instructor!'
