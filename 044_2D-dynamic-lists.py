import random, time, os

#stores random numbers for bingo card
bingoList = []

#places random numbers in bingoList
for i in range(0,8):
  i = random.randint(1,90)
  if i in bingoList:
    continue
  else:
    bingoList.append(i)

bingoList.sort()

print(bingoList)

#assigns generated random numbers to bingo card
bingoCard = [ [ bingoList[0], bingoList[1], bingoList[2]],
              [ bingoList[3], "BINGO", bingoList[4]],
              [ bingoList[5], bingoList[6], bingoList[7]] ]

print(bingoCard)

#pretty print of bing card
def printBingo():
  print("""===BINGO CARD===
""")
  for row in bingoCard:
    for item in row:
      print(f"{item:^10}", end=" | ")
    print()
  print()

counter = 0

while True: 
  printBingo()
  number = int(input("What number comes next? "))
  print()

  for row in range(3):
    for item in range(3):
      if bingoCard[row][item] == number:
        bingoCard[row][item] = "X"
        counter += 1
  
  if counter == 8:
    print("You have won!")
    break

  time.sleep(1)
  os.system("clear")
