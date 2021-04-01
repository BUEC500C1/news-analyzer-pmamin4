import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("localhost", 27017)

mydb = client["database4"]
mycoll = mydb["table4"]

list4 = [{"date": "2/2/20", "articlename" : "article0", "Author": "Purvis1", "publisher":"fox0"},
        {"date": "2/23/20", "articlename" : "article1", "Author": "Purvis2", "publisher":"fox1"},
        {"date": "3/3/20", "articlename" : "article2", "Author": "Purvis3", "publisher":"fox2"},
        {"date": "4/2/20", "articlename" : "article3", "Author": "Purvis4", "publisher":"fox3"},
        {"date": "5/23/20", "articlename" : "article4", "Author": "Purvis5", "publisher":"fox4"},
        {"date": "6/3/20", "articlename" : "article5", "Author": "Purvis6", "publisher":"fox5"}]




#x = mycoll.insert_many(list4)
#dblist = client.list_database_names()
#print(dblist)
for x in mycoll.find():
    print(x)