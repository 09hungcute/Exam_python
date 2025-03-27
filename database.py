from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["medical_service"]

def get_next_sequence(name):
    counter = db.counters.find_one_and_update(
        {"_id": name},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=True
    )
    return counter["seq"]
