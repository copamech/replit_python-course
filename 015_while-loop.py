exit = ""
while exit != "yes":
  animal = input("What animal do you want? ")

  if animal == "cow":
    print("Mooo!")
  elif animal == "pig":
    print("Oink oink!")
  elif animal == "sheep":
    print("Baaaaaa!")
  elif animal == "dog":
    print("Woof!")
  else:
    print("I don't know which sound that animal makes. Try again.")
  
  exit = input("Do you want to exit? ")
