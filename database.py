import pymongo
from pymongo import MongoClient
from flask import Flask
import datetime
client = MongoClient()

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
collection = db.test_collection

users = db.users
user = {"birthdate": birthday,
        "name": name,
        "number": number,
        "email": email,
        "contact1":  contact1,
        "contact2": contact2,
        "contactname1": contactname1,
        "contactname2": contactname2,
        "contact1number": contact1number,
        "contact2number": contact2number
        }
        

users.insert_one(user)
for i in users.find():
    print(i)
    
    
@app.route('/new_user')
    def signup():
        if not session.get(' birthday','name', 'number', 'email'):
            abort(401)
        new_user = {"birthdate": birthday,
            "name": name,
            "number": number,
            "email": email
            }
        db.insert_one(new_user)
        flash('Account successfully created')
        return redirect('opening.html')