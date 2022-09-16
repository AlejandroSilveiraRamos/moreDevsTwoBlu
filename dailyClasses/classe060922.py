#dojo game 06 learn - sum of year earnings
#variables
s = 0
months = ("January", "February",  "March", "April", "May", "June", "July", "August", "September","October", "November", "December")
nextMonth = 0

#for to looping all months
for c in range (0, 12):
    monthGain = int(input("How much do you in {} sell? ".format(months[nextMonth])))
    nextMonth += 1
    s += monthGain
print(f"Your total gain in this year: {s}")    


   




