from pymongo import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Atlas connection URI with the new password
#uri = "mongodb+srv://saritabk:EbFPDnprpiaKKIpD@tech-coder.pam2wzq.mongodb.net/?retryWrites=true&w=majority&appName=tech-coder"
uri = "mongodb+srv://saritabk:EbFPDnprpiaKKIpD@tech-coder.pam2wzq.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoDB client with the Server API version
client = MongoClient(uri, server_api=ServerApi('1'))

# Access database and collection
db = client.todo_db
collection = db["todo_data"]
