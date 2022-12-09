# Used list.count( ) function for the first time

import os, time

inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  print("ERROR: There is no existing inventory document, using a blank list.")

def addItem():
  item = input("Item to add: ").strip().title()
  inventory.append(item)
  print(f"{item} has been added to your inventory.")

def removeItem():
  item = input("Input the item to remove: ").strip().title()
  inventory.remove(item)
  print(f"{item} has been removed from your inventory.")

def viewItems():
  item = input("Input the item to view: ").strip().title()
  itemCount = inventory.count(item)
  print(f"You have {itemCount} {item}.")
  
while True:
  time.sleep(2)
  os.system("clear")
  print("🌟RPG Inventory🌟")
  print("=========")
  print()
  menu = input("1. Add item\n2. Remove item\n3. View items\n")
  print()
  if menu == "1":
    addItem()
  elif menu == "2":
    removeItem()
  elif menu == "3":
    viewItems()
  else:
    print("That is not an option. Please choose an available option (1, 2, or 3).")

  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()
