#!/usr/bin/python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pprint

mongo_uri = "mongodb://127.0.0.1:27017"
mongo_db = "stdhops"
collection_name = "houseeeee"

client = MongoClient(mongo_uri)
db = client[mongo_db]

pipeline = [
    { "$match": {} },
    { "$addFields": {
        "district_code": {
            "$let": {
                "vars": {
                    "districtInString": [
                        " ", 
                        "พระนคร",
                        "ดุสิต",
                        "หนองจอก",
                        "บางเขน",
                        "บางรัก",
                        "บางกะปิ",
                        "ปทุมวัน",
                        "ป้อมปราบศัตรูพ่าย",
                        "พระโขนง",
                        "มีนบุรี",
                        "ลาดกระบัง",
                        "ยานนาวา",
                        "สัมพันธวงศ์" ,
                        "พญาไท",
                        "ธนบุรี",
                        "บางกอกใหญ่",
                        "ห้วยขวาง",
                        "คลองสาน",
                        "ตลิ่งชัน",
                        "บางกอกน้อย",
                        "บางขุนเทียน",
                        "ภาษีเจริญ" ,
                        "หนองแขม",
                        "ราษฎร์บูรณะ",
                        "บางพลัด",
                        "ดินแดง",
                        "บึงกุ่ม",
                        "สาทร",
                        "บางซื่อ",
                        "จตุจักร",
                        "บางคอแหลม",
                        "ประเวศ",
                        "คลองเตย",
                        "สวนหลวง",
                        "จอมทอง",
                        "ดอนเมือง",
                        "ราชเทวี",
                        "ลาดพร้าว",
                        "วัฒนา",
                        "บางแค",
                        "หลักสี่",
                        "สายไหม",
                        "คันนายาว",
                        "สะพานสูง",
                        "วังทองหลาง",
                        "คลองสามวา",
                        "บางนา",
                        "ทวีวัฒนา",
                        "ทุ่งครุ",
                        "บางบอน"]
                },
                "in": {
                    "$indexOfArray": ["$$districtInString", "$district"]}
                }
            },
        "location": {
            "type": "Point",
            "coordinates": [
                {"$convert":
                    {
                        "input": {"$arrayElemAt": ["$latlng", 1]},
                        "to": "double",
                        "onError": "$null"
                    }
                },
                {"$convert":
                    {
                        "input": {"$arrayElemAt": ["$latlng", 0]},
                        "to": "double",
                        "onError": "$null"
                    }
                }]
            }
        }
    },
    # project
    {"$project": {
        "location": 1,
        "district_code": 1,
        "id": 1,
        "latlng": 1,
        "district": 1,
        "price": 1,
        "room": 1
        }
    },
    { "$out": "loc" }
]

pprint.pprint(list(db[collection_name].aggregate(pipeline)))
 