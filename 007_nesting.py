character = input("Who is your favorite character on Lord of the Rings? ")
if character == "Gandalf":
  print("Of course you like Gandalf, he's a wizard.")
  path = input("Do you prefer Gandalf the Grey or Gandalf the White? ")
  if path == "Grey":
    print("Ah yes, the early days were best.")
  else:
    print("The peak of his powers!")
elif character == "Frodo":
  print("The most heroic of them all...")
else:
  print("No one cares about that character.")
