#set fixed variables 

from unicodedata import name


firstName = "alejandro"
lastName = "silveira ramos"
fullName = firstName + " " + lastName
age = "21"

#print variables, using .format to allocate the variables / .tile to formate text all first letter to Uppercase

print("Your full name is {} and your age {}".format((fullName.title()), (age)))

