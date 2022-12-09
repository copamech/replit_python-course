import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "extension", "recording", "horoscope", "survival"]

wordChosen = random.choice(listOfWords)

guessList = []

print("🌟Hangman🌟")
print()
print("""Rules of the game:

- The computer will randomly select a word from the list of ten words.
- Guess one letter at time. The computer will reveal if the letter is in the word and where.
- The computer will also keep track of each or your letter guesses and how many times you've picked a letter that is not in the word.
- If you guess more than six letters that are not in the word, you lose.""")
print()

def printHang():
  guessProgress = wordChosenr
  for i in guessProgress:
    if i not in guessList:
      guessProgress[i] = "_"
  print(guessProgress)

lives = 6

while True:
  guess = input("Choose a letter: ").lower()
  
  if guess in guessList:
    print("You've already tried that letter.")
    continue
  
  guessList.append(guess)

  if guess in wordChosen:
    print("Correct!")
  else:
    print("Nope, not in there")
    lives -=1

  print()
  allLetters = True

  for i in wordChosen:
    if i in guessList:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
      
  if allLetters:
    print()
    print(f"You won with {lives} lives left")
    break

  if lives <= 0:
    print()
    print(f"You ran out of lives! The answer was {wordChosen}")
    break
  else:
    print()
    print(f"{lives} lives left")
    print()
        
