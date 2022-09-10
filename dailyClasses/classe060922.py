#dojo game 06 learn

#user
#name = input("Write your first name: ")
#lastName = input("now your last name: ")
#fullName = name + " " + lastName
#age = input("Now write your age: ")

#sum of earnings
contador = 0

while contador < 2:
    print(f'Valor do contador é {contador}')
    monthGain = int(input("How much do you sell last month? "))
    
    total = None

    if total == None:
        total = monthGain
        print("entrou {} {}".format(total, monthGain))
    else:
        monthGain = total + monthGain

    contador += 1
else:
    print("Your name: {} \n Your age: {}  \n total ganho no mes {}".format((fullName.title()), (age), (monthGain)))

   




