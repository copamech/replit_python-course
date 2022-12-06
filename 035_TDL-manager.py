import os, time

myToDo = []

def printTDL():
  print()
  for item in myToDo:
    print(item)
  print()

while True:
  print("To Do List Manager")
  print()
  menu = input("What would you like to do?\n\n1. Add an item\n2. Remove an item\n3. Edit an item\n4. View your TDL\n5. Delete your TDL\n")
  print()
  if menu == "1":
    item = input("What are you adding to your list?\n")
    if item in myToDo:
      print(f"{item} is already in your list.")
    else:
      myToDo.append(item)
  elif menu == "2":
    item = input("What are you removing from your list?\n")
    if item in myToDo:
      confirm = input("Are you sure you want to remove {item} from your list? Y/N\n")
      if confirm == "Y":
        myToDo.remove(item)
    else:
      print()
      print(f"{item} is not in your list.")
  elif menu == "3":
    printTDL()
    item = input("Which item would you like to edit from your list?\n")
    newItem = input("What do you want to change it to?\n")
    for i in range(0,len(myToDo)):
      if myToDo[i] == item:
        myToDo[i] = newItem
  elif menu == "5":
    myToDo = []
    
    
  print()
  print("Your TDL")
  printTDL()
  time.sleep(3)
  os.system("clear")
