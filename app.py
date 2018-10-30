
from flask import Flask, jsonify, request
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


# @app.route("/addinstructor")
# def addInstructor():
#     return "add instructor route"


# @app.route("/login")
# def login():
#     return "login page"


# //////////////////////////      INSTRUCTOR ROUTES      ////////////////////////


@app.route('/instructors', methods=['GET'])
def get_all_instructors():
    instructor = mongo.db.instructors

    output = []

    for q in instructor.find({}):

        output.append(
            {'First name': q['firstName'], 'Last name': q['lastName']})

    return jsonify({'result': output})


@app.route('/instructors/<name>', methods=['GET'])
def get_one_instructor(name):
    instructor = mongo.db.instructors

    q = instructor.find_one({'firstName': name})

    output = []

    if q:
        output = {'first name': q['firstName'],
                  'last name': q['lastName'], 'Current DZ': q['currentDZ']}

    return jsonify({'result': output})


@app.route('/instructors', methods=['POST'])
def add_instructor():
    instructor = mongo.db.instructors

    firstName = request.json['firstName']
    lastName = request.json['lastName']
    currentDZ = request.json['currentDZ']

    instructor_id = instructor.insert(
        {'currentDZ': currentDZ, 'firstName': firstName, 'lastName': lastName})
    new_instructor = instructor.find_one({'_id': instructor_id})

    output = {'firstName': new_instructor['firstName'],
              'lastName': new_instructor['lastName'],
              'currentDZ': new_instructor['currentDZ']}

    return jsonify({'result': output})


# //////////////////////////      LOCATION ROUTES      ////////////////////////


# //////////////////////////      REVIEW ROUTES      ////////////////////////
if __name__ == '__main__':
    app.run(debug=True)
