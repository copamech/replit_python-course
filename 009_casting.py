year = int(input("What year were you born? "))
if year < 1925:
  print("You're so old I don't know what to call you!")
elif year < 1947:
  print("You are a Traditionalist.")
elif year < 1965:
  print("You are a Baby Boomer.")
elif year < 1982:
  print("You are from Generation X.")
elif year < 1996:
  print("You are a Millenial.")
elif year < 2016:
  print("You are from Generation Z, the Zoomers!")
else:
  print("You're too young for us to care about you right now.")
