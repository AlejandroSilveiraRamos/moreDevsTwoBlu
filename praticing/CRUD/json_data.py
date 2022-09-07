import json

def save_data(json_data):
    with open('json\course.json', 'w') as f:
        json.dump(json_data, f, indent=4)