import csv

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  total = 0
  for row in reader:
    total += float(row["Cost"])*int(row["Quantity"])
    total = round(total,2)

print("🌟Shop $$ Tracker🌟")
print()
print(f"Your shop took ${total} today.")
