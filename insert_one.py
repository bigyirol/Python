#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.testdb

    # Añadir un coche
    new_car = {"name": "Citroen","price": 2600 }
    db.cars.insert_one(new_car)
