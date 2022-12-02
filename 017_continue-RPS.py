# from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print("First player to win three rounds wins the game.")
print()

counter1 = 0
counter2 = 0

while True:
  if counter1 == 3 or counter2 == 3:
    print("Final results: P1 with", counter1, "victories, P2 with", counter2, "victories.")
    exit()
  else:
    print()
    print("ROUND", (counter1 + counter2 +1))
    print()
    player1Move = input("Player 1 > ")
    print()
    player2Move = input("Player 2 > ")
    print()
    if player1Move=="R":
      if player2Move=="R":
        print("You both picked Rock, draw!")
      elif player2Move=="S":
        print("Player1 smashed Player2's Scissors into dust with their Rock!")
        counter1 += 1
      elif player2Move=="P":
        print("Player1's Rock is smothered by Player2's Paper!")
        counter2 += 1
      else:
        print("Invalid Move Player 2!")
    elif player1Move=="P":
      if player2Move=="R":
        print("Player2's Rock is smothered by Player1's Paper!")
        counter1 += 1
      elif player2Move=="S":
        print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
        counter2 += 1
      elif player2Move=="P":
        print("Two bits of paper flap at each other. Dissapointing. Draw.")
      else:
        print("Invalid Move Player 2!")
    elif player1Move=="S":
      if player2Move=="R":
        print("Player 2's Rock makes metal-dust out of Player1's Scissors")
        counter2 += 1
      elif player2Move=="S":
        print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
      elif player2Move=="P":
        print("Player1's Scissors make confetti out of Player2's paper!")
        counter1 += 1
      else:
        print("Invalid Move Player 2!")
    else:
      print("Invalid Move Player 1!")
      continue
