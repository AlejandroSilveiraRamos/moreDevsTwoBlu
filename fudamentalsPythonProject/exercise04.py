#exercise 4
#variables
salary = float(input("How much is your first month salary? "))
salarySecond = float(input("How much is your second month salary? "))
salaryThird = float(input("How much is your third month salary? "))
salaryFourth = float(input("How much is your fourth month salary? "))
salaryAll = salary + salarySecond + salaryThird + salaryFourth

#printing using polymorphism
print("="*10, "calculator", "="*10)
print("First salary: {:.2f} \n Second salary: {:.2f} \n Third salary: {:.2f} \n Fourth salary: {} \n Total: {:.2f}".format(salary, salarySecond, salaryThird, salaryFourth, salaryAll))
print("="*10, "total", "="*10)