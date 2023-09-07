# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:10:09 2023

@author: Shabista
"""

import pymongo
from pymongo import MongoClient

# Connect to the MongoDB server running on localhost at port 27017
client = MongoClient('localhost', 27017)
# Access a specific database, for example, "TeachForIndia"
db = client['TeachForIndia']
# Access a collection, for example, "registration"
collection = db['registration']

# Find all documents in the collection
cursor = collection.find()

def insert(name,phone,email,location,language,days):
    document = {"name": name, "phone":phone, "email":email,"location":location,"languages":language,"days":days}
    collection.insert_one(document)
    return True
 
# Insert a document into the collection
document = {"name": "John", "age": 30}
result = collection.insert_one(document)

# Iterate through the result cursor to access documents
for document in cursor:
    print(document)


client.close()