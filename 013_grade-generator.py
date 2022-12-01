test = input("What is the name of your test? ")
max = int(input("What is the maximum score for the test? "))
score = int(input("What score did you receive? "))

result = float(score/max)
percent = round((result*100), 2)

if(percent >= 90):
  grade = "A"
elif(percent < 90) and (percent >= 80):
  grade = "B"
elif(percent < 80) and (percent >= 70):
  grade = "C"
elif(percent < 70) and (percent >= 80):
  grade = "C"
else:
  grade = "F"

print("You received a", percent, "% on the test, which is a grade of", grade)
