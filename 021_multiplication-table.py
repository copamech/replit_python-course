print("Math challenge!")
print()
print("Choose a number for multiplication table test. You will be asked to show give an answer to each multiplication question up to 10.")
number = int(input("> "))

counter = 0
score = 0

for i in range(number, 11*number, number):
  counter += 1
  print()
  print(counter, "x", number, "= ")
  answer = int(input("> "))
  if answer == i:
    print("Correct!")
    score += 1
  else:
    print("Incorrect.")

if score == 10:
  print("Congratulations! You received a perfect score! 😝")
else:
  print("You got a", score, "out of 10.")
    
