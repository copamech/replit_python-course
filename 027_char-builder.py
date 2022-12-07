import os, time, random

def roll(sides):
  result = random.randint(1, sides)
  return result

def healthroll():
  health = (roll(6) * roll(12) / 2) + 10
  return health

def strengthroll():
  strength = (roll(6) * roll(12) / 2) + 12
  return strength

while True:
  print("Legendary Character Builder")
  character = input("Name Your Legend: ")
  charType = input("Choose your character type (Human, Elf, Wizard, Orc): ")
  print()
  time.sleep(1)
  os.system("clear")
  print(character)
  print("HEALTH:", healthroll())
  print("STRENGTH:", strengthroll())
  print()
  print("May your name go down in Legend.")
  print()
  gameOn = input("Would you like to create another character?" )
  if gameOn != "yes":
    break
