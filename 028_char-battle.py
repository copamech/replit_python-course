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
  print("⚔️ LEGEND VS. LEGEND ⚔️")
  print()
  character1 = input("Name Your Legend: ")
  charType1 = input("Choose your character type (Human, Elf, Wizard, Orc): ")
  print()
  char1Health = int(healthroll())
  char1Strength = int(strengthroll())
  print(character1)
  print("HEALTH:", char1Health)
  print("STRENGTH:", char1Strength)
  print()
  print("Who are they battling?")
  print()
  character2 = input("Name Your Legend: ")
  charType2 = input("Choose your character type (Human, Elf, Wizard, Orc): ")
  print()
  char2Health = int(healthroll())
  char2Strength = int(strengthroll())
  print(character2)
  print("HEALTH:", char2Health)
  print("STRENGTH:", char2Strength)
  time.sleep(2)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  counter = 0
  while char1Health > 0 and char2Health > 0:
    counter += 1
    print("ROUND", counter)
    time.sleep(2)
    print()
    char1Roll = roll(6)
    char2Roll = roll(6)
    damage = int((abs(char1Strength - char2Strength) + 1))
    if char1Roll > char2Roll:
      char2Health -= damage
      print(character1, "wins Round", counter)
      print(character2, "takes a hit, with", damage, "damage")
    elif char2Roll > char1Roll:
      char1Health -= damage
      print(character2, "wins Round", counter)
      print(character1, "takes a hit, with", damage, "damage")
    else:
      print("Round", counter, "ends in a draw.")
    print()
    print(character1)
    print("HEALTH:", char1Health)
    print()
    print(character2)
    print("HEALTH:", char2Health)
    print()
    if char1Health > 0 and char2Health > 0:
      print("And they're both standing for the next round!")
      time.sleep(7)
      os.system("clear")
    elif char1Health > char2Health:
      print("Oh no", character2, "has died!")
      print(character1, "destroyed", character2, "in", counter, "rounds and emerges victorious!")
    else:
      print("Oh no", character1, "has died!")
      print(character2, "destroyed", character1, "in", counter, "rounds and emerges victorious!")
  print()
  gameOn = input("Would you like to play again?" )
  if gameOn != "yes":
    break
    
