# multiplication table

num = float(input("Insert any number to show in multiplication table: "))

contador = 0

while contador < 11:
    print(" {} X {} = {} ".format( num, contador, num*contador ))

    contador += 1
else:
    print("All results already")
    
