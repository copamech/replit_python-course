print("=== Your Wacky Recipe Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up a wacky
recipe, totally copyright free 😭""")
print()
food = input("Name a type of food: ")
plant = input("Name a type of plant: ")
method = input("Name a method of cooking: ")
burned = input("Name a word to describe burned food: ")
item = input("Name a household item: ")
print()
print(method, food, "with", burned, plant, "on a bed of", item)
