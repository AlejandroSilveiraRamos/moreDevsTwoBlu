#Exercise 02

#variables
name = input("What is your first name? ")
lastName = input("What is your last name? ")
fullName = name + " " + lastName

age = input("What is your age? ")
height = input("What is your height? (In Meters) ")
weight = input("What is your weight? (In Kg) ") 
salary = input("How much is your month salary ")

#print and format interpolation variables
print(f"Name: {fullName}  Age: {age} Height: {height} m  Weight: {weight} Kg  Salary: {salary} $")