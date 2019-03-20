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
    # convert ตารางวา to ตารางเมตร
    # {"$match": {"area": { "$regex": 'วา$'} } },
    # {"$addFields": {"convertedArea": {"$multiply": [{"$toInt": {"$trim": {"input": "$area", "chars": " ตารางวา"} } }, 2]}}},
    {"$match": {} },
    # clean listed date
    {"$addFields": {"splited_date": {"$split": [{"$arrayElemAt": [{"$split": ["$date", " | "]}, 1] }, " "]}}},
    {"$addFields": {"monthString": {"$arrayElemAt": ["$splited_date", 4] }}},
    {"$addFields": {
        "month": {
            "$let": {
                "vars": {
                    "monthsInString": [" ","มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฏาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน" ,"ธันวาคม"]
                },
                "in": {
                    "$indexOfArray": ['$$monthsInString', '$monthString']
                }
            }
        }
    }},
    {"$addFields": {"day": {"$toInt": {"$arrayElemAt": ["$splited_date", 3] }}}},
    {"$addFields": {"year": {"$subtract": [{"$toInt": {"$arrayElemAt": ["$splited_date", 5] }}, 543]}}},
    {"$addFields": {"listed_date": {"$dateFromParts": {
        "year": "$year", "month": "$month", "day": "$day"
    }}}},
    # project
    {"$project": {
        "listed_date": 1,
        "convertedArea": 1,
        "id": 1,
        "latlng": 1,
        "price": 1,
        "room": 1
    }},
    { "$out" : "authors" }
    ]
# pprint.pprint(list(db[collection_name].aggregate(pipeline)))

# data = list(db['houseeeee'].aggregate([{"$group" : {"_id":"$district", "count":{"$sum":1}}}]))
data = list(db[collection_name].aggregate([
    {
        "$match": {
            "price": {"$regex": "ให้เช่า"}
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
    {
        "$out": "rental_price"
    }
]))


