#!/usr/bin/env python
import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient


mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['local']
collection_name = 'upload'
db=mongo_db[collection_name]

reader = csv.DictReader(open('C:/Users/Administrator/Desktop/Senior/GitCrawl/stdhops-crawler/crawlerbot/upload/test.csv', 'r'))
header = ["id","name","location","type","size","floor","yearbuilt","bed","bath","latlong"]
result = {}
for r in reader:
    for field in header:
#        if(r[field]!=header):
#            result[field]="null"
        result[field]=r[field]
    
    db.insert_one(result)
