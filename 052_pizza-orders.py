import os, time

orders = []

try:
  f = open("pizza-order.txt", "r")
  orders = eval(f.read())
  f.close()
except:
  print("ERROR: No existing orders list, using a blank list.")

def add():
  print()
  name = input("Name: ").title()
  toppings = input("Toppings: ")
  size = input("Size (s/m/l): ").lower()
  while True:
    try:
      quantity = int(input("Quantity: "))
      break
    except:
      print("""You must input a numerical character for "quantity", try again.""")
  cost = 0
  if size == "s":
    cost = 10
  elif size == "m":
    cost = 15
  else:
    cost = 20
  total = cost*quantity
  total = round(total, 2)
  row = [name, toppings, size, quantity, total]
  orders.append(row)

def view():
  h1 = "Name"
  h2 = "Toppings"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:^20}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
  for row in orders:
    print(f"{row[0]:^20}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  time.sleep(1)

while True:
  time.sleep(2)
  os.system("clear")
  print("🌟Nemo's Pizza🌟")
  print()
  menu = input("1. Add an order\n2. View orders\n")
  
  if menu == "1":
    add()

  elif menu == "2":
    view()

  else:
    print("That is not an option.")

  f = open("pizza-order.txt", "w")
  f.write(str(orders))
  f.close()
