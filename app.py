
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

# //////////////////////////      INSTRUCTOR ROUTES      ////////////////////////


@app.route('/instructors', methods=['GET'])
def get_all_instructors():
    instructor = mongo.db.instructors

    output = []

    for q in instructor.find({}):

        output.append(
            {'First name': q['firstName'], 'Last name': q['lastName']})

    return jsonify({'result': output})


# @app.route('/instructors/<name>', methods=['GET'])
# def get_one_instructor(name):
#     instructor = mongo.db.instructors

#     q = instructor.find_one({'firstName': name})

#     output = []

#     if q:
#         output = {'first name': q['firstName'],
#                   'last name': q['lastName'], 'Current DZ': q['currentDZ']}

#     return jsonify({'result': output})


@app.route('/instructors/<dz>', methods=['GET'])
def get_all_instructors_from_dz(dz):
    instructor = mongo.db.instructors

    output = []

    for q in instructor.find({'currentDZ': dz}):

        output.append(
            {'firstName': q['firstName'], 'lastName': q['lastName']})

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


@app.route('/locations', methods=['GET'])
def get_all_locations():
    locations = mongo.db.locations

    output = []

    for q in locations.find({}):

        output.append(
            {'dzName': q['dzName'], 'dzCity': q['dzCity']})

    return jsonify({'result': output})


@app.route('/dznames', methods=['GET'])
def get_all_dzNames():
    locations = mongo.db.locations

    output = []

    for q in locations.find({}):

        output.append(
            {'dzName': q['dzName']})
    # return output
    return jsonify({'result': output})


@app.route('/locations/<name>', methods=['GET'])
def get_one_location(name):
    locations = mongo.db.locations

    q = locations.find_one({'dzName': name})

    output = []

    if q:
        output = {'dzName': q['dzName'],
                  'dzCity': q['dzCity'], 'dzState': q['dzState']}

    return jsonify({'result': output})


@app.route('/locations', methods=['POST'])
def add_location():
    locations = mongo.db.locations

    dzName = request.json['dzName']
    dzCity = request.json['dzCity']
    dzState = request.json['dzState']

    location_id = locations.insert(
        {'dzState': dzState, 'dzName': dzName, 'dzCity': dzCity})
    new_location = locations.find_one({'_id': location_id})

    output = {'dzName': new_location['dzName'],
              'dzCity': new_location['dzCity'],
              'dzState': new_location['dzState']}

    return jsonify({'result': output})


# //////////////////////////      REVIEW ROUTES      ////////////////////////


@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    reviews = mongo.db.reviews

    output = []

    for q in reviews.find({}):

        output.append(
            {'reviewerName': q['reviewerName'], 'review': q['review'], 'locationJumped': q['locationJumped'], 'instructorFirst': q['instructorFirst'], 'instructorLast': q['instructorLast']})

    return jsonify({'result': output})


@app.route('/reviews/<first>/<last>', methods=['GET'])
def get_reviews_for_instructor(first, last):
    reviews = mongo.db.reviews

    output = []

    for q in reviews.find({'instructorFirst': first, 'instructorLast': last}):

        output.append(
            {'instructorFirst': q['instructorFirst'], 'instructorLast': q['instructorLast'],
             'review': q['review']})

    return jsonify({'result': output})


@app.route('/reviews/<userName>', methods=['GET'])
def get_reviews_for_username(userName):
    reviews = mongo.db.reviews

    output = []

    for q in reviews.find({'userName': userName}):

        output.append(
            {'review': q['review']})

    return jsonify({'result': output})


@app.route('/reviews', methods=['POST'])
def add_review():
    reviews = mongo.db.reviews

    locationJumped = request.json['locationJumped']
    instructorFirst = request.json['instructorFirst']
    instructorLast = request.json['instructorLast']
    review = request.json['review']
    reviewerName = request.json['reviewerName']

    review_id = reviews.insert(
        {'instructorLast': instructorLast, 'locationJumped': locationJumped, 'instructorFirst': instructorFirst, 'review': review, 'reviewerName': reviewerName})
    new_review = reviews.find_one({'_id': review_id})

    output = {'locationJumped': new_review['locationJumped'],
              'instructorFirst': new_review['instructorFirst'],
              'instructorLast': new_review['instructorLast'],
              'review': new_review['review'],
              'reviewerName': new_review['reviewerName']}

    return jsonify({'result': output})

    # /////////////////////////////////    USERS ROUTES /////////////////////////////


@app.route('/users/<userName>/<password>', methods=['GET'])
def get_user_login(userName, password):
    users = mongo.db.users

    output = []

    for q in users.find({'userName': userName, 'password': password}):

        output.append(
            {'firstName': q['firstName'], 'lastName': q['lastName']})

    return jsonify({'result': output})


@app.route('/users/<userName>', methods=['GET'])
def get_user_info(userName):
    users = mongo.db.users

    output = []

    for q in users.find({'userName': userName}):

        output.append(
            {'firstName': q['firstName'], 'lastName': q['lastName'], 'userName': q['userName'], 'bio': q['bio'], 'currentDZ': q['currentDZ']})

    return jsonify({'result': output})


@app.route('/users/<userName>', methods=['POST'])
def add_user_info(userName):
    users = mongo.db.users

    currentDZ = request.json['currentDZ']
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    userName = request.json['userName']
    password = request.json['password']
    bio = request.json['bio']
    photo = request.json['photo']

    user_id = users.insert(
        {'firstName': firstName, 'lastName': lastName, 'currentDZ': currentDZ, 'userName': userName, 'password': password, 'bio': bio, 'photo': photo})
    new_user = users.find_one({'_id': user_id})

    # output = {'locationJumped': new_user['locationJumped'],
    #           'instructorFirst': new_user['instructorFirst'],
    #           'instructorLast': new_user['instructorLast'],
    #           'user': new_user['review'],
    #           'reviewerName': new_user['reviewerName']}

    # return jsonify({'result': output})
    return ('working')


if __name__ == '__main__':
    app.run(debug=True)
