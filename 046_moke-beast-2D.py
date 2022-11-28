print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()

beastiary = {}

#pretty Print of beast card
def prettyPrint():
  print()
  for record, key in beastiary.items():
    
    #change color of MokeBeast card depending on beast type
    if beastiary[record]["type"] == "Fire":
      print("\033[0;31m", end="")
    elif beastiary[record]["type"] == "Earth":
      print("\033[0;33m", end="")
    elif beastiary[record]["type"] == "Air":
      print("\033[0;00m", end="")
    elif beastiary[record]["type"] == "Water":
      print("\033[0;34m", end="")
    elif beastiary[record]["type"] == "Spirit":
      print("\033[0;32m", end="")
    else:
      print("\033[0;37m", end="")

    #print out beast card
    print(f"=== {record} ===")
    for subKey, subValue in key.items():
      print(f"{subKey}\t: {subValue}")
    print("\033[0;37m", end="")
    print()

while True:
  name = input("Name: ").strip().title()
  type = input("Type: ").strip().title()
  move = input("Special Move: ").strip().title()
  hp = input("HP: ").strip()
  mp = input("MP: ").strip()

  beastiary[name] = {"type": type,
                     "move": move,
                     "hp": hp,
                     "mp": mp }

  prettyPrint()
  
  again = input("Create another beast? (y/n): ").strip().lower()
  if again[0] == "y":
    print()
    continue
  else:
    break
