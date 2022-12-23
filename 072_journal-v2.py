from replit import db
import datetime, os, time, random

timestamp = datetime.datetime.now()

keys = db.keys()

# to delete keys in database
# for key in keys:
#  del db[key]

# print(list(keys))

# Creates username and password if none exists
def addUser():
  print("Welcome to the Journal Tracker. Please create a username and password.\n")
  username = input("Username: ")
  password = input("Password: ")
  if username in keys:
    print("Error: username already exists.")
    return
  salt = random.randint(1000,9999)
  saltPass = f"{password}{salt}"
  hashPass = hash(saltPass)
  db[username] = {"hashed password": hashPass, "salt": salt}
  print("Details stored.")
  time.sleep(1)
  os.system("clear")

# Checks to see if user credentials match entry in database
def login():
  print("Welcome to the Journal Tracker. Please use your credentials to log in.\n")
  username = input("Username: ")
  password = input("Password: ")
  if username not in keys:
    print("ERROR: username does not exist. Exiting program.")
    exit()
  salt = db[username]["salt"]
  saltPass = f"{password}{salt}"
  hashPass = hash(saltPass)
  if hashPass == db[username]["hashed password"]:
    print("Login successful.")
  else:
    print("Access denied.")
    exit()
  time.sleep(1)
  os.system("clear")

# Adds journal entry
def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

# Views journal entry
def viewEntry():
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break

# The first time the diary is run, the user must create a username and password. If the database is empty, assume this is the first time the diary has been run and create a username and password.
if list(keys):
  login()
else:
  addUser()

while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
