def subroutine(color, word):
  if color=="red":
    print("\033[0;31m", word, sep="", end="")
  elif color=="yellow":
    print("\033[1;33m", word, sep="", end="")
  elif color=="blue":
    print("\033[0;34m", word, sep="", end="")
  elif color=="green" :
    print("\033[0;32m", word, sep="", end="")
  else:
    print("\033[0;0m", word, sep="", end="")

print("Super Subroutine")
print()
print("With my ", end="")
subroutine("green", "new program ")
subroutine("reset", "I can just call red ('and') ")
subroutine("red", "and ")
subroutine("reset", "that word will appear in the color I set it to.")
print()
print()

print("With no ", end="")
subroutine("yellow", "weird gaps")
subroutine("reset", ".")

print()
print()
print("Epic.")
