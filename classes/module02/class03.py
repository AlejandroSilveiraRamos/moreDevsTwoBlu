# multiplication table

num = float(input("Insert any number to show in multiplicatin table: "))

contador = 0

while contador < 9:
    print(" {} X {} = {} ".format( num, contador, num*contador ))

    contador += 1
else:
    print("Acabou")
    
