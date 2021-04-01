import requests

BASE = "http://127.0.0.1:5000/"

data = [{"numbers": 100, "words": 10, "filename": "purvisfiel", "characters": 23, "font": "calibir", "language": "english"},
        {"numbers": 156, "words": 33, "filename": "allelujah", "characters": 333, "font": "roman", "language": "spanish"},
        {"numbers": 10440, "words": 1044, "filename": "set", "characters": 2333, "font": "ariel", "language": "jap"}]

#for i in range(len(data)):
#    response = requests.put(BASE + "text/" + str(i), data[i])
#    print(response.json())


#input()
response = requests.patch(BASE + "text/1" , {"characters": 95})
print(response.json())