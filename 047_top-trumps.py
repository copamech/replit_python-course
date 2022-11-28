#Top Trumpers - Marvel battle 1992 trading cards. Power = "Fighting Ability" from the cards.

import os, time, random

longshot = {"strength": 2, "intelligence": 2, "power": 5, "speed": 3}
spiderman = {"strength": 4, "intelligence": 4, "power": 4, "speed": 3}
sabretooth = {"strength": 2, "intelligence": 2, "power": 7, "speed": 1}
psylocke = {"strength": 2, "intelligence": 2, "power": 5, "speed": 2}
warpath = {"strength": 6, "intelligence": 2, "power": 4, "speed": 2}


cards = {"Longshot":longshot, "Spider-Man":spiderman, "Sabretooth":sabretooth, "Psylocke":psylocke, "Warpath":warpath}

while True:
  print("""Welcome to the Top Trumps "1992 Marvel Trading Card" Simulator!""")
  print()
  choice = input("Choose your card:\n\n1. Longshot\n2. Spider-Man\n3. Sabretooth\n4. Psylocke\n5. Warpath\n\n")

  if choice == "1":
    player = "Longshot"
  elif choice == "2":
    player = "Spider-Man"
  elif choice == "3":
    player = "Sabretooth"
  elif choice == "4":
    player = "Psylocke"
  elif choice == "5":
    player = "Warpath"
  else:
    print("That is not an option. Try again.")
    time.sleep(3)
    os.system("clear")
    continue
  
  print()
  computer = random.choice(list(cards.keys()))
  print(f"Computer has picked {computer}")
  print()
  stat = input("Choose your attribute:\n\n1. Strength\n2. Intelligence\n3. Power\n4. Speed\n\n")
  print()
  
  if stat == "1":
    compare = "strength"
  elif stat == "2":
    compare = "intelligence"
  elif stat == "3":
    compare = "power"
  elif stat == "4":
    compare = "speed"
  else:
    print("That is not an option. Try again.")
    time.sleep(3)
    os.system("clear")
    continue

  print(f"{player} {compare}: {cards[player][compare]}")
  print(f"{computer} {compare}: {cards[computer][compare]}")
  print()

  if cards[player][compare] > cards[computer][compare]:
    print(f"You ({player}) win")
  elif cards[player][compare] < cards[computer][compare]:
    print(f"The computer ({computer}) wins")
  else:
    print("It's a draw")

  print()
  again = input("Again? y/n: ")

  if again == "y":
    os.system("clear")
    continue
  else:
    break
  
