from flask import Flask, jsonify

from database.database import db
from helpers.helpers import loop_through_response

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
        loop_through_response(all_restaurants_arr, get_all_restaurants)
        return jsonify(all_restaurants_arr)
    except Exception as e: 
        print(f"An error has occurred while trying to retrieve results: {e}")
        return jsonify({"error": f"An error has occurred while trying to retrieve results: {e}"})


# Find a restaurant by name
@app.route('/restaurant/<name>')
def find_restaurant(name):
    try:
        # the find() method finds the 'restaurants' collection
        # the optional arguments do the following - pos. 0 ({"name": name}), returns documents matching the parameter - pos. 1 ({"_id": 0}) removes the _id property, or else an exception is thrown due to the way _id is formatted
        restaurants_by_name_arr = []
        find_restaurant_by_name = db.restaurants.find({"name": name},  {"_id": 0})
        loop_through_response(restaurants_by_name_arr, find_restaurant_by_name)
        return jsonify(restaurants_by_name_arr)
    except Exception as e:
        print(f"An error has occurred while trying to retrieve results: {e}")


# Find restaurants by cuisine type
@app.route('/restaurant/cuisine/<cuisine>')
def find_restaurant_by_cuisine(cuisine):
    try:
        # the find() method finds the 'restaurants' collection
        # the optional arguments do the following - pos. 0 ({"cuisine": cuisine}), returns documents matching the parameter - pos. 1 ({"_id": 0}) removes the _id property, or else an exception is thrown due to the way _id is formatted
        # the limit() method limits the results to 20 since the collection has over 25k results
        restaurants_by_cuisine_arr = []
        find_restaurant_by_cuisine = db.restaurants.find({"cuisine": cuisine},  {"_id": 0}).limit(20)
        loop_through_response(restaurants_by_cuisine_arr, find_restaurant_by_cuisine)
        return jsonify(restaurants_by_cuisine_arr)
    except Exception as e:
        print(f"An error has occurred while trying to retrieve results: {e}")


# HTTP 404 not found catch all route
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return jsonify({"error": "HTTP 404 - Page Not Found"}), 404


# HTTP 500 internal server error catch all route
@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return jsonify({"error": "HTTP 500 - An Internal Server Error has occurred"}), 500
    

# HTTP 502 gateway timeout error catch all route
@app.errorhandler(502)
def page_not_found(e):
    # note that we set the 502 status explicitly
    return jsonify({"error": "HTTP 502 - An Gateway Timeout has occurred"}), 502
