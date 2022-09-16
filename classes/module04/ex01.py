from unicodedata import name


#Dictionary
'''
nameList = {"name": "Alejandro", "lastName": "Ramos"}
item = { "_id": "1", "name": "Iphone 11", "category": "Smartphone"}


print(nameList["name"], "\n", item["name"])
 
nameList["age"] = 18

print(nameList["age"], "\n", item["name"])

'''
#add to a dictionary
'''
firstName = str(input("Whats your name? "))
lastName = str(input("Whats your  last name? "))
age = int(input("Whats your age? "))
job = str(input("Whats your job? "))

person = {}

person["name"] = firstName
person["lastName"] = lastName
person["age"] = age
person["job"] = job

print(person)

'''

orderNumeric = {1: "one", 2: "three"}
newOrder = {2: "two"}

# updates the value of key 2
orderNumeric.update(newOrder)

print(orderNumeric)

newOrder = {3: "three"}

# adds element with key 3
orderNumeric.update(newOrder)

print(orderNumeric)

