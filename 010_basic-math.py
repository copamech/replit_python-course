myBill = float(input("What was the bill?: "))
myTip = int(input("What percent tip would you like to add? i.e. 15, 18, 20, etc. "))
total = myBill * ((100 + myTip) / 100)
total = round(total, 2)
print("Your total cost is $", total)
numberOfPeople = int(input("How many people?: "))
answer = total / numberOfPeople
answer = round(answer, 2)
print("You all owe $", answer)
