import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("localhost", 27017)

mydb = client["database3"]
mycoll = mydb["table3"]

list3 = [{"filename": "jay", "numbers": 5000, "words": 1650, "characters": 27893, "font": "calibi", "language": "english"},
        { "filename": "Setsuna", "numbers": 456156, "words": 12333,"characters": 365433, "font": "times roman", "language": "spanish"},
        { "filename": "Lockon", "numbers": 19940, "words": 1999,"characters": 2020, "font": "ariel", "language": "japanese"}]


#x = mycoll.insert_many(list3)

#dblist = client.list_database_names()

#print(dblist)
#for x in mycoll.find():
#    print(x)