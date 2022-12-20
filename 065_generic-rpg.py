# Playing with classes and subclasses to create characters in an RPG.

class character:
  name = None
  HP = 100
  MP = 50
  
  def __init__(self, name):
    self.name = name
    
  def print(self):
    print(f"{self.name}\nHP: {self.HP}\nMP: {self.MP}")
    
  def setStats(self, HP, MP):
    self.HP = HP
    self.MP = MP

class player(character):
  nickname = None
  lives = 3

  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def print(self):
    print(f"{self.name}\nNickname: {self.nickname}\nHP: {self.HP}\nMP: {self.MP}\nLives: {self.lives}\n")

  def status(self):
    if self.lives > 0:
      print(f"{self.name} is alive with {self.lives} lives left.")
      return True
    else:
      print(f"{self.name} is dead 💀")
      return False

class enemy(character):
  enType = None
  strength = None

  def __init__(self, name, enType, strength):
    self.name = name
    self.enType = enType
    self.strength = strength

class orc(enemy):
  speed = None

  def __init__(self, name, speed):
    self.enType = "Orc"
    self.HP = 70
    self.MP = 10
    self.strength = 130
    self.name = name
    self.speed = speed

  def print(self):
    print(f"{self.enType}\nName: {self.name}\nHP: {self.HP}\nMP: {self.MP}\nStrength: {self.strength}\nSpeed: {self.speed}\n")

class vampire(enemy):
  day = True

  def __init__(self, name, day):
    self.enType = "Vampire"
    self.HP = 60
    self.MP = 110
    self.strength = 85
    self.name = name
    self.day = day

  def print(self):
    print(f"{self.enType}\nName: {self.name}\nHP: {self.HP}\nMP: {self.MP}\nStrength: {self.strength}\nDaytime?: {self.day}\n")

print("🌟Generic RPG🌟")
print()

link = player("Link")
link.print()
link.status()
print()

print("===Enemies remaining===\n")

dracula = vampire("Dracula", True)
nosferatu = vampire("Nosferatu", True)

ugnar = orc("Ugnar", 100)
wegler = orc("Wegler", 30)
moktu = orc("Moktu", 55)

dracula.print()
nosferatu.print()
ugnar.print()
wegler.print()
moktu.print()

