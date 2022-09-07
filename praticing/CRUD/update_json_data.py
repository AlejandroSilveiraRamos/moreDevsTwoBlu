from praticing.CRUD.json_data import save_data
from praticing.CRUD.load_json_data import load_data

json_data = load_data()

id = input('Enter Id to find course in json')
data = {
	"yearSalary": 4300,
	"age": w2,
	"name": "Wagner"
}
json_data[id] = data # updating data
save_data(json_data) # saving the json file