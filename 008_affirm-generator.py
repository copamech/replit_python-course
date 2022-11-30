print("""== AFFIRM ===
The power of positive thinking compels you to respond to the following questions then you shall be...
rewarded!""")
name = input("What is your name? ")
day = input("What day of the week is it? ")
prefer = input("Do you prefer swimming or biking? ")
if day == "monday":
  print("MONDAY MANIAC!!")
  motiv = input("Are you ready to get after it?! ")
  if motiv == "yes":
    print("Put it here,", name, "!!! Let's go", prefer, "!")
  else:
    print("Turn that frown upside down,", name, "!")
elif day == "saturday" or day == "sunday":
  print("Relax and enjoy your weekend,", name, "! You deserve it!")
else:
  print("Stay on your grind,", name, "! Everybody's working for the weekend!")
