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
  menu = input("Would you like to add or remove an item from your TDL? To simply view the TDL, enter any other command.\n")
  print()
  if menu == "add":
    item = input("What are you adding to your list?\n")
    myToDo.append(item)
  elif menu == "remove":
    item = input("What are you removing from your list?\n")
    if item in myToDo:
      myToDo.remove(item)
    else:
      print()
      print(f"{item} is not in your list.")
  print()
  print("Your TDL")
  printTDL()
  time.sleep(3)
  os.system("clear")
