#get input to set a variables and set a type of

firstName = input("What it is your first name? ")
lastName = input("Now your last name? ")
fullName = firstName + " " + lastName

age = int(input("How about your age? "))
salary = float(input("How about your salary? "))

#print the variables and type

print("Your full name is {}, your age {} and your salary {:.2f}".format((fullName.title()), (age), (salary)), type(age))