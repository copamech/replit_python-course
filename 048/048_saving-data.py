print("🌟HIGH SCORE TABLE🌟")
print()

table = {}

while True:
  initials = input("Input your initials: ")
  score = input("Input your score (out of 100,000): ")
  print("Your score has been added to the high score table.")

  f = open("high-scores.txt", "a+")
  f.write(f"{initials} {score}\n")
  f.close()
  
  again = input("Add another? y/n: ")

  if again == "y":
    continue
  else:
    break
