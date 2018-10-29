
import os
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
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
