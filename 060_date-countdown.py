import datetime

today = datetime.date.today()

print("🌟Event Countdown Timer🌟")
print()
event = input("Input the event name: ").strip().capitalize()
year = int(input("Input the event year: "))
month = int(input("Input the event month: "))
day = int(input("Input the event day: "))

eventDate = datetime.date(year, month, day)

delta = abs(eventDate - today)
delta = delta.days

if delta > 0:
  print(f"{event} is just {delta} day(s) away!")
elif delta < 0:
  print(f"{event} already happened {delta} day(s) ago.")
else:
  print("Your event is today!")
