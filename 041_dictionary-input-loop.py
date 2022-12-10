print("🌟Website Rating🌟")
print()

webInfo = {"name": None, "url": None, "description": None, "rating": None}

for i in webInfo.keys():
  webInfo[i] = input(f"{i}: ").strip()

print()
print("===Details===")
print()

for i, j in webInfo.items():
  print(f"{i}: {j}")
