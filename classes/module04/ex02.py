#while
const = "no"

while const == "no":
    thing = str(input("Type anything: "))
    print(thing)
    const = str(input("Do you wanna leave? "))
    if const != "no" and const != "yes":
        print("Not a command try again? ")
        const = str(input("Do you wanna leave? "))
       
print("your out")