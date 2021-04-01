import requests

BASE = "http://127.0.0.1:5000/"


data = [{"filename":"a", "filetype":"pdb", "owner": "purvis","editor":"jayson", "viewer":"naith"}, 
        {"filename":"b", "filetype":"trf", "owner": "jayson","editor":"naith", "viewer":"Purvis"},
        {"filename":"c", "filetype":"docx", "owner": "nate","editor":"Purvis", "viewer":"Jayson"}]

for i in range(7,19):
    response = requests.patch(BASE + "file/" + str(i))
    print(response.json())
