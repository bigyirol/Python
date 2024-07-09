from pymongo import MongoClient

model_tree = [
    { "_id": "MongoDB", "parent": "Databases" },
    { "_id": "dbm", "parent": "Databases" },
    { "_id": "Databases", "parent": "Programming" },
    { "_id": "Languages", "parent": "Programming" },
    { "_id": "Programming", "parent": "Books" },
    { "_id": "Books", "parent": None }
]

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.testdb

    res = db.model_tree.insert_many(model_tree)
    print(res)
