print("Replit Login System")
print()

userCred = "Satoshi"
passCred = "wtf1971"

def login():
  while True:
    user = input("What is your username?: ")
    password = input("What is your password?: ")
    if user == userCred and password == passCred:
      print()
      print("Welcome to Replit!")
      break
    else:
      print()
      print("Whoops! I don't recognize that username or password. Try again!")
      print()
      continue

login()

