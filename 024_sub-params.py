import random

print("Infinity Dice 🎲")
print()

sides = int(input("How many sides to your dice?: "))
gameOn = "yes"

def rollDice(sides):
  print()
  print("You rolled", random.randint(1, sides))

while gameOn == "yes":
    rollDice(sides)
    gameOn = input("Roll again? ")
