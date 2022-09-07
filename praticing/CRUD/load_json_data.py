import json

def load_data():
    with open('services/dataBase.json') as f: 
        return json.load(f)