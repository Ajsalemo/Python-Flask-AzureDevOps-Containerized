from flask import Flask, json, jsonify

from database.database import db

app = Flask(__name__)


# Home route
@app.route('/')
def hello_world():
    return 'Python-AzureDevOps-Containerized'


# Get all AirBNB rental data
@app.route('/all_restaurants')
def all_restaurants():
    try:
        all_restaurants_arr = []
        # the find() method finds the 'restaurants' collection
        # the optional arguments do the following - pos. 0 ({}), returns the entire collection - pos. 1 ({"_id": 0}) removes the _id property, or else an exception is thrown due to the way _id is formatted
        # the limit() method limits the results to 20 since the collection has over 25k results
        get_all_restaurants = db.restaurants.find({}, {"_id": 0}).limit(20)
        for restaurants in get_all_restaurants:
            # Append a document to the array for each iteration
            all_restaurants_arr.append(restaurants)
        return jsonify(all_restaurants_arr)
    except Exception as e: 
        print(f"An error has occurred while trying to retrieve results: {e}")
        return jsonify({"error": f"An error has occurred while trying to retrieve results: {e}"})


# Find a restaurant by name
@app.route('/restaurant/<name>')
def find_restaurant(name):
    print(name)
    return jsonify({"message": f"Searching for {name}"})


# HTTP 404 not found catch all route
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return jsonify({"error": "HTTP 404 - Page Not Found"}), 404
    

