sentence = input("What sentence do you want to rainbow-ify?\n")

RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
YELLOW = "\033[1;33m"
DEFAULT = "\033[0;0m"

for letter in sentence:

  if letter.lower() == "r":
    print(RED, end='')

  if letter.lower() == "g":
    print(GREEN, end='')

  if letter.lower() == "b":
    print(BLUE, end='')

  if letter.lower() == "p":
    print(PURPLE, end='')

  if letter.lower() == "y":
    print(YELLOW, end='')

  if letter.lower() == " ":
    print(DEFAULT, end='')

  print(letter, end='')
