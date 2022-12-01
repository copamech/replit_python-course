from getpass import getpass as input
print("""Welcome to the ultimate Rock, Paper, Scissors Showdown!
This is a 2 player game. Choose your weapon (type "R", "P", or "S") and wait for the next player to challenge you then see who is victorious!""")
player_1 = input("Player 1, what do you choose? ")
player_2 = input("Ok. Player 2, what do you choose? ")

if player_1 == "R":
  if player_2 == "R":
    print("🥌🥌 Tie game! Try again.")
  elif player_2 == "P":
    print("🥌📃 Victory goes to Player 2!")
  else:
    print("🥌✂ Victory goes to Player 1!")
elif player_1 == "P":
  if player_2 == "R":
    print("📃🥌 Victory goes to Player 1!")
  elif player_2 == "P":
    print("📃📃 Tie game! Try again.")
  else:
    print("📃✂ Victory goes to Player 2!")
elif player_1 == "S":
  if player_2 == "R":
    print("✂🥌 Victory goes to Player 2!")
  elif player_2 == "P":
    print("✂📃 Victory goes to Player 1!")
  else:
    print("✂✂ Tie game! Try again.")
else:
  print("Follow the directions!")
