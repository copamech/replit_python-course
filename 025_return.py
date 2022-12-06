import random

print("⚔️ Character Stats Generator ⚔️")
print()

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def rollSixEight():
  rollSix = rollDice(6)
  rollEight = rollDice(8)
  health = rollSix * rollEight
  return health

gameOn = "yes"

while gameOn == "yes":
  name = input("Name your warrior: ")
  health = str(rollSixEight())
  print("Your character's health is", health, "hp")
  print()
  gameOn = input("Would you like to create another character? ")
