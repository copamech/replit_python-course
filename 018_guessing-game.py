print("The One-Million-To-One Guessing Game")
print("Pick any whole number between 1 and 1,000,000. We will tell you if your pick is too high or too low before you guess again. How many rounds will it take you to guess the number?")
print()

number = 397805
counter = 0

while True:
  guess = int(input("What is your guess? "))
  if guess <= 0:
    print("You must pick a number between 1 and 1,000,000 (inclusive). Restart the game.")
    exit()
  else:
    if guess == number:
      print("Congratulations! You have successfully guessed the right number. It took you", (counter + 1), "attempt(s).")
      exit()
    else:
      if guess > number:
        print("Too high. Guess again.")
        print()
      else:
        print("Too low. Guess again.")
        print()
      counter += 1
      continue
