print("""Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)""")
print()

counter = 1
while True:
  print("I don't want to waste your _____")
  word = input()
  if word == "time":
    break
  else:
    print("Nope, try again.")
    counter += 1
    print()
print("You got it! That only took you", counter, "attempt(s).")
