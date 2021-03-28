from dotenv import load_dotenv

from flask import Flask, jsonify

from database.database import db


app = Flask(__name__)
load_dotenv()


# Home route
@app.route('/')
def hello_world():
    return 'Python-AzureDevOps-Containerized'


# Get all AirBNB rental data
@app.route('/all_restaurants')
def all_restaurants():
    # the find() method finds the 'restaurants' collection
    # the limit() method limits the results to 20 since the collection has over 25k results
    get_all_restaurants = db.restaurants.find().limit(20)
    for restaurants in get_all_restaurants:
        print(restaurants)
    return "Test"

