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
        "email": email,
        "contact1":  contact1,
        "contact2": contact2,
        "contactname1": contactname1,
        "contactname2": contactname2,
        
        
        
        

posts.insert_one(post)
for i in posts.find():
    print(i)