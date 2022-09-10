#Exercise 03

#variables
name = str(input("What is your first name? "))
lastName = str(input("What is your last name? "))
fullName = name + " " + lastName

age = int(input("What is your age? "))
height = float(input("What is your height? (In Meters) "))
weight = float(input("What is your weight? (In Kg) ")) 
salary = float(input("How much is your month salary "))

#print and function insert variables 
print("Name: {} Age: {} Height: {}  Weight: {} Salary: {}".format(fullName, age, height, weight, salary))