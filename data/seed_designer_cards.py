import json
from bson import ObjectId

def seed_designer_cards(db):
    with open("data/EmptyCup.DesignerCards.json") as f:
        data = json.load(f)
    for item in data:
        item["_id"] = ObjectId(item["_id"]["$oid"])
    db.DesignerCards.insert_many(data)
    print("✅ Seeded DesignerCards.")
