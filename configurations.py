from pymongo import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Atlas connection URI (replace <username>, <password>, <cluster-url> with actual values)
MONGO_URI = "mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority"

# Initialize MongoDB client with the Server API version
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db=client.todo_db
collection=db["todo_data"]