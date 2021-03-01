import requests

BASE = "http://127.0.0.1:5000/"


data= [{"date": "2/2/2", "articlename" : "article", "Author": "Purvis", "publisher":"fox"},
        {"date": "2/23/2", "articlename" : "article", "Author": "Purvis", "publisher":"fox"},
        {"date": "2/2/2", "articlename" : "article", "Author": "Purvis", "publisher":"fox"}]


response = requests.delete(BASE + "news/100")
print(response)
response = requests.get(BASE + "news/100")
print(response.json())



