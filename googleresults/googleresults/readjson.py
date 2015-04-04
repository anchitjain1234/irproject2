import json
from pprint import pprint

with open('items2.json') as data_file:    
    data = json.load(data_file)

for i in range(len(data)):
    print(data[i]["link"])
