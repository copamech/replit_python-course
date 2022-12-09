nameList = []

def printList():
  print()
  for i in nameList:
    print(i)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in nameList:
    nameList.append(name)
  else:
    print("Error: duplicate name")
  printList()
