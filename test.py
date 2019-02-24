from pymongo import MongoClient
import pprint

mongo_uri = 'mongodb://127.0.0.1:27017'
mongo_db = 'stdhops'
collection_name = 'houseeeee'

client = MongoClient(mongo_uri)
db = client[mongo_db]

pipeline = [
    {"$match": {"area": { "$regex": 'วา$'} } },
    {"$project": {"date": 1, "district": 1, "area": {"$trim": {"input": "$area", "chars": " ตารางวา"} } } },
    {"$addFields": {"convertedArea": {"$multiply": [{"$toInt": "$area"}, 2]}}},
    {"$project": { "district": 1, "area": 1, "convertedArea": 1, "date": {"$split": ["$date", "|"]}}}]

pprint.pprint(list(db[collection_name].aggregate(pipeline)))


