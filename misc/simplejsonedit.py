#simply edit json, not recomended for constant use
import json

def pushItem(file, items, indent=4):
    with open(file, 'w') as data:
        json.dump(items, data, indent=indent)

def delItem(file, item):
    with open(file) as data_file:
        data = json.load(data_file)

    del data[item]

    with open(file, 'w') as data_file:
        data = json.dump(data, data_file)

def allItems(file):
    with open(file) as data_file:
        data = json.load(data_file)

    return data
