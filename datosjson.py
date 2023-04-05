import json

with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)
print(ourjson)
