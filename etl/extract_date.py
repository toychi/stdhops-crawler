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
    { "$match": {} },
    # clean listed date
    { "$addFields": {
        "splited_listdate": {
            "$split": [{"$arrayElemAt": [{"$split": ["$date", " | "]}, 1]}, " "]
            },
        "splited_updatedate": {
            "$split": [{"$arrayElemAt": [{"$split": ["$date", " | "]}, 2]}, " "]
            }
        }
    },
    {"$addFields": {
        "monthString": {
            "$arrayElemAt": ["$splited_listdate", 4]
            },
        "upmonthString": {
            "$arrayElemAt": ["$splited_updatedate", 4]
            }
        }
    },
    {"$addFields": {
        "month": {
            "$let": {
                "vars": {
                    "monthsInString": [" ", "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฏาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
                },
                "in": {
                    "$indexOfArray": ['$$monthsInString', '$monthString']
                }
            }
        },
        "upmonth": {
            "$let": {
                "vars": {
                    "monthsInString": [" ", "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฏาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
                },
                "in": {
                    "$indexOfArray": ['$$monthsInString', '$upmonthString']
                }
            }
        }
    }},
    {"$addFields": {
        "day": {"$toInt": {"$arrayElemAt": ["$splited_listdate", 3]}},
        "upday": {"$toInt": {"$arrayElemAt": ["$splited_updatedate", 3]}}
        }
    },
    {"$addFields": {
        "year": {"$subtract": [{"$toInt": {"$arrayElemAt": ["$splited_listdate", 5]}}, 543]},
        "upyear": {"$subtract": [{"$toInt": {"$arrayElemAt": ["$splited_updatedate", 5]}}, 543]}
        }
    },
    {"$addFields": {
        "listed_date": {"$dateFromParts": {"year": "$year", "month": "$month", "day": "$day"}},
        "updated_date": {"$dateFromParts": {"year": "$upyear", "month": "$upmonth", "day": "$upday"}}
        }
    },
    # project
    {"$project": {
        "listed_date": 1,
        "updated_date": 1,
        "convertedArea": 1,
        "id": 1,
        "latlng": 1,
        "price": 1,
        "room": 1
        }
    },
    { "$out": "house" }
]

pprint.pprint(list(db[collection_name].aggregate(pipeline)))
