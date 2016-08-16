import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient()

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
collection = db.test_collection

posts = db.posts
post = {"birthdate": birthday,
        "name": full_name,
        "number": phone_number,
        "email": your_email,
        "contacts": contact
        "contactname "
        
        

posts.insert_one(post)
for i in posts.find():
    print(i)