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
    # match only rental house provided in monthly rate
    {
        "$match": {
            "price": {"$regex": "ขาย"}
        }
    },
    # change district Thai name to district code
    # field: "district_code"
    {"$addFields": {
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
                        "สัมพันธวงศ์",
                        "พญาไท",
                        "ธนบุรี",
                        "บางกอกใหญ่",
                        "ห้วยขวาง",
                        "คลองสาน",
                        "ตลิ่งชัน",
                        "บางกอกน้อย",
                        "บางขุนเทียน",
                        "ภาษีเจริญ",
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
    # clean listed date and updated date to Date objects
    # field: "listed_date"
    # field: "updated_date"
    {"$addFields": {
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
    }
    },
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
    # convert price string to integer
    # field: priceint
    {"$addFields": {
        "priceint": {
            "$convert":
                    {
                        "input": {
                            "$reduce": {
                                "input": {'$split': [{'$trim': {'input': "$price", 'chars': "ขาย บาท"}}, ',']},
                                'initialValue': '',
                                'in': {
                                    '$concat': [
                                        '$$value',
                                        '$$this']
                                }
                            }
                        },
                        "to": "int",
                        "onError": "$null"
                    }
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
        "room": 1,
        "listed_date": 1,
        "updated_date": 1,
        "convertedArea": 1,
        "priceint": 1
    }
    },
    # export to new collection
    # collection: thaihowntown_sale
    {"$out": "thaihometown_sale"}
]

pprint.pprint(list(db[collection_name].aggregate(pipeline)))
