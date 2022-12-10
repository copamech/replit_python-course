import random

bingoList = []

for i in range(0,8):
  i = random.randint(1,90)
  if i in bingoList:
    continue
  else:
    bingoList.append(i)

bingoList.sort()

bingoCard = [ [bingoList[0], bingoList[1], bingoList[2]],
              [bingoList[3], "BINGO", bingoList[4]],
              [bingoList[5], bingoList[6], bingoList[7]] ]

def printBingo():
  for row in bingoCard:
    print(row)

printBingo()
