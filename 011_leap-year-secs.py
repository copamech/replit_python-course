print("""How many seconds in a year? Depends on which year and if it's a leap year.
A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400.""")
year = int(input("What year is it? "))

if (year % 100 == 0) and (year % 400 == 0):
    print("{0} is a leap year".format(year))
    seconds = 366 * 24 * 60 * 60
    print("There are", seconds, "in this year.")
  
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
    seconds = 366 * 24 * 60 * 60
    print("There are", seconds, "in this year.")
  
else:
    print("{0} is not a leap year".format(year))
    seconds = 365 * 24 * 60 * 60
    print("There are", seconds, "in this year.")
