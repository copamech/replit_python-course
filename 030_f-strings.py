print("30 Days Down")
print()
print("What have you thought of each of the 30 days of Python coding challenges so far?")
print()

for i in range (1,31):
  response = input(f"Day {i} of 30:\n")
  print()
  feedback = f"You thought Day {i} was {response}." 
  print(f"{feedback:^70}")
  print()
