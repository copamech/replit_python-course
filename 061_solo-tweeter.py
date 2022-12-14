# This code uses Replit DB and will not work outside of Replit

from replit import db
import datetime, os, time

timestamp = datetime.datetime.now()

# to clear out database, activate this code
#keys = db.keys()
#for key in keys:
#  del db[key]

def addTweet():
  tweet = input("🐥: ")
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")

def viewTweet():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for key in matches:
    print(db[key])
    print()
    time.sleep(0.5)
    counter += 1
    if counter%10 == 0:
      viewMore = input("View next 10? (y/n): ").strip().lower()
      if viewMore == "n":
        break
  time.sleep(1)
  os.system("clear")

while True:
  print("Solo-Tweeter")
  menu = input("1. Add tweet\n2. View tweets\n")

  if menu == "1":
    addTweet()
  elif menu == "2":
    viewTweet()
  else:
    print("That is not an option, try again.")
