import requests

BASE = "http://127.0.0.1:5000/"


data= [{"date": "2/2/2", "articlename" : "article", "Author": "Purvis", "publisher":"fo457x"},
        {"date": "2/23/2", "articlename" : "arti455cle", "Author": "Pur123vis", "publisher":"fo456x"},
        {"date": "3/3/1", "articlename" : "artic23le", "Author": "Purv457is", "publisher":"fo123x"}]



response = requests.delete(BASE + "news/100")
print(response)
response = requests.get(BASE + "news/100")
print(response.json())
