import os
import uuid

from flask import Flask
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

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
