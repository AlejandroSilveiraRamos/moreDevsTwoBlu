
from praticing.CRUD.load_json_data import load_data

json_data = load_data()

id = input('Enter Id to Delete the item associated with it')
del json_data[id]

save_json_data(json_data)