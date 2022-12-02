print("List Generator")
print()

start = int(input("Start at: "))
end = int(input("End before: "))
incr = int(input("Increment between values: "))

for i in range(start, end, incr):
  print(i)
