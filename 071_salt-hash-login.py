# Applying salting and hashing to passwords to create a login system. Storing keys and values in Replit DB

from replit import db
import random, os, time

keys = db.keys()

def addUser():
  time.sleep(1)
  os.system("clear")
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

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  if username not in keys:
    print("Error: username does not exist.")
    time.sleep(1)
    os.system("clear")
    return
  salt = db[username]["salt"]
  saltPass = f"{password}{salt}"
  hashPass = hash(saltPass)
  if hashPass == db[username]["hashed password"]:
    print("Login successful.")
  else:
    print("Access denied.")
    return
  time.sleep(1)
  os.system("clear")

while True:
  print("🌟Login System🌟")
  print()
  menu = input("1. Add User\n2. Login\n")
  if menu == "1":
    addUser()
  else:
    login()
