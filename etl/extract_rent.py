#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pprint

mongo_uri = 'mongodb://127.0.0.1:27017'
mongo_db = 'stdhops'
collection_name = 'houseeeee'

client = MongoClient(mongo_uri)
db = client[mongo_db]

pipeline = [
    {
        "$match": {
            "price": {"$regex": "บาท/เดือน"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "id": 1,
            "district": 1,
            "priceint": {
                "$reduce": {
                    "input": {'$split': [{'$trim': {'input': "$price", 'chars': "ให้เช่า บาท/เดือน"}}, ',']},
                    'initialValue': '',
                    'in': {
                        '$concat': [
                            '$$value',
                            '$$this']
                    }
                }
            }
        }
    },
    { "$out": "rental_price" }
]

pprint.pprint(list(db[collection_name].aggregate(pipeline)))
