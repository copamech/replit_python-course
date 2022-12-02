print("🌟Current Leader🌟")
print()
print("Analyzing high scores......")
print()

maxScore = [["User", 0]]

f = open("high-scores","r")

while True:
  contents = f.readline()

  if contents == "":
    break
  
  contents = contents.split()
  player = contents[0]
  score = int(contents[1])

  if score > maxScore[0][1]:
    maxScore[0][0] = player
    maxScore[0][1] = score

print(f"Current leader is {maxScore[0][0]} {maxScore[0][1]}")
