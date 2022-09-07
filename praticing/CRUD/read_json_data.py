from praticing.CRUD.load_json_data import load_data


id = input('Enter Id to find Id person in json')

json_data = load_data()	

def get_one_item_from_json(id):
	for x in json_data:
		if x['id'] == id:
			return x