import os

from dotenv import load_dotenv

load_dotenv()

from flask_pymongo import pymongo

# Environment variables
MONGO_ATLAS_USERNAME = os.environ.get("MONGO_ATLAS_USERNAME")
MONGO_ATLAS_PASSWORD = os.environ.get("MONGO_ATLAS_PASSWORD")
MONGO_ATLAS_CLUSTER = os.environ.get("MONGO_ATLAS_CLUSTER")
MONGO_ATLAST_DATABASE = os.environ.get("MONGO_ATLAST_DATABASE")

# Connect to a Mongo Atlas cluster with this connection string
CONN_STR=f"mongodb+srv://{MONGO_ATLAS_USERNAME}:{MONGO_ATLAS_PASSWORD}@{MONGO_ATLAS_CLUSTER}/{MONGO_ATLAST_DATABASE}?retryWrites=true&w=majority"
# Set the max connection pool size to 128
# Set the max idle time for connections in the pool to 30 seconds
client = pymongo.MongoClient(CONN_STR, maxPoolSize=128, maxIdleTimeMS=30000)
db = client.get_database(MONGO_ATLAST_DATABASE)
