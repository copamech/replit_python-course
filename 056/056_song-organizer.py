import csv, os, time



with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    dir = os.listdir()
    artist = row["Artist(s)"]
    song = row["Song"]
    print(f"Adding {song} by {artist} to file directory...")

    if artist not in dir:
      os.mkdir(artist)
    else:
      pass
      
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()

    time.sleep(1)
    os.system("clear")

print("Song organization complete!")
