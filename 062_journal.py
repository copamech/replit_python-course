#This program is incomplete (#3 menu option) and #2 menu option isn't working properly, seems to be related to Replit DB problems

from replit import db
import datetime, os, time

timestamp = datetime.datetime.now()

# to clear out database, activate this code
#keys = db.keys()
#for key in keys:
#  del db[key]


def addEntry():
  time.sleep(1)
  os.system("clear")
  print(f"Journal entry for {timestamp}")
  print()
  entry = input("✒️: ")
  db[timestamp] = entry
  time.sleep(1)
  os.system("clear")

def viewLatest():
  entries = db.keys()
  for key in entries:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    
    {db[key]}""")
    print()
    viewMenu = input("1. View previous entry\n2. Exit to main menu\n")
    if viewMenu == "2":
      break
  
def viewSpecific():
  print("What is the entry date you wish to view? ")
  year = int(input("Year: "))
  month = int(input("Month: "))
  day = int(input("Day: "))
  entryDate = datetime.date(year, month, day)
  

correctPassword = "happydaze"
passwordEntered = input("Enter your password: ").strip()
print()
if passwordEntered != correctPassword:
  print("Incorrect password. Exiting program.")
  exit()
else:
  pass

while True:
  os.system("clear")
  print("""===Journal Tracker===
  """)
  menu = input("1. Add entry\n2. View latest entry\n3. View specific entry\n")
  if menu == "1":
    addEntry()
  elif menu == "2":
    viewLatest()
  elif menu == "3":
    viewSpecific()
  else:
    print("That is not an option. Try again.")

