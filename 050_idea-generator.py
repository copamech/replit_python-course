import os, time, random

while True:
  print("🌟Idea Storage🌟")
  print()
  menu = input("Add an idea or see a random idea? (a/r): ")

  if menu == "a":
    print()
    idea = input("Input your idea > ")
    f = open("my-ideas", "a+")
    f.write(f"{idea}\n")
    f.close()
    print()
    print("Your idea has been stored.")

  elif menu == "r": 
    print()
    f = open("my-ideas", "r")
    content = f.read().split("\n")
    content.remove("")
    f.close()
    idea = random.choice(content)
    print(idea)
    
  else:
    print()
    print("That is not an option.")
  
  time.sleep(2)
  os.system("clear")
