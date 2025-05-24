import json
from pymongo import MongoClient
from bson import ObjectId

def seed_designer_cards():
    client = MongoClient("mongodb://localhost:27017/")  
    db = client["EmptyCup"] 
    collection = db["designer_cards"]
    if collection.count_documents({}) == 0:
        with open("app/data/EmptyCup.DesignerCards.json", "r") as f:
            raw_data = json.load(f)

        formatted_data = []
        for item in raw_data:
            item["_id"] = ObjectId(item["_id"]["$oid"])
            formatted_data.append(item)

        collection.delete_many({}) 
        collection.insert_many(formatted_data)
        print("✅ Designer cards seeded successfully.")