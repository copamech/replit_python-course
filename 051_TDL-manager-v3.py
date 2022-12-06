# To Do List Manager using 2D Lists, storing task name, due date, priority

import time, os

TDL = []

f = open("TDL.txt", "r")
TDL = eval(f.read())
f.close()

def TDLPrint():
  for row in TDL:
    for item in row:
      print(item, end="\t|\t")
    print()

def priorityPrint(priority):
  for row in TDL:
    if priority in row:
      for item in row:
        print(item, end="\t|\t")
  print()

while True:
  print("🌟Life Organizer🌟")
  print()
  menu = input("What do you want to do?\n\n1. Add an item\n2. View list\n3. Remove an item\n4. Edit an item\n\n")
  print()

  if menu == "1":
    task = input("What is the task? ").strip().capitalize()
    due = input("When is the task due? ").strip()
    priority = input("What is the task priority? (High, Medium, Low): ").strip().capitalize()
    row = [task, due, priority]
    TDL.append(row)
    print()
    print("This task has been added to your list.")
    print()

  if menu == "2":
    viewMenu = input("What do you want to view?\n\n1. Full list\n2. Priority list (High, Medium, Low)\n\n")
    print()

    if viewMenu == "1":
      TDLPrint()
      print()
      time.sleep(2)

    if viewMenu == "2":
      viewPriority = input("Which priority do you want to view? (High, Medium, Low)\n\n").strip().capitalize()
      print()
      if viewPriority == "High":
        priorityPrint("High")
        time.sleep(2)

      elif viewPriority == "Medium":
        priorityPrint("Medium")
        time.sleep(2)
      
      elif viewPriority == "Low":
        priorityPrint("Low")
        time.sleep(2)

      else:
        print("That is not an option. Please select again.")
        print()

  if menu == "3":
    item = input("Which item do you want to remove? ").strip().capitalize()
    print()
    
    for row in TDL:
      
      if item in row:
        TDL.remove(row)
        print(f"'{item}' has been removed from your list.")
        print()

      else:
        break
    
    print(f"'{item}' is not in your list.")
    print()

  if menu == "4":
    item = input("Which item do you want to edit? ").strip().capitalize()
    print()

    for row in TDL:

      if item in row:
        TDL.remove(row)
        task = input("New task name: ").strip().capitalize()
        due = input("New task due date: ").strip()
        priority = input("New task priority (High, Medium, or Low): ").strip().capitalize()
        row = [task, due, priority]
        TDL.append(row)
        print()

      else:
        print(f"'{item}' is not in your list.")
        print()
  
  time.sleep(2)
  os.system("clear")

  f = open("TDL.txt", "w")
  f.write(str(TDL))
  f.close()
