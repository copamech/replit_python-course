from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False
  while True:
    stop_playback = int(input("Press 2 to stop playback and go back to the menu: "))
    if stop_playback == 2:
      source.paused = True
      return
    else:
      continue
    
while True:
  os.system("clear")
  print ("""🎵 MyPOD Music Player
  Press 1 to Play
  Press 2 to Exit
  Press anything else to see the menu again.""")
  time.sleep(1)
  choice = int(input("> "))
  if choice == 1:
    print("Enjoy!")
    play()
  elif choice == 2:
    break
  else:
    continue

print("Goodbye!")
