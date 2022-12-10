print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()

beastiary = {"name": None,
             "type": None,
            "special move": None,
            "HP": None,
            "MP": None }

for name, value in beastiary.items():
  beastiary[name] = input(f"{name}: ").strip().title()

print()

for key, value in beastiary.items():
  if key == "type":
    if value == "Fire":
      print("\033[0;31m", end="")
    elif value == "Earth":
      print("\033[0;33m", end="")
    elif value == "Air":
      print("\033[0;00m", end="")
    elif value == "Water":
      print("\033[0;34m", end="")
    elif value == "Spirit":
      print("\033[0;32m", end="")
    else:
      print("\033[0;37m", end="")
  else:
    print("\033[0;00m", end="")
  print(f"{key: <15}: {value}")
