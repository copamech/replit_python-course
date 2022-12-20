class job():
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = float(salary)
    self.hoursWorked = int(hoursWorked)

  def details(self):
    print()
    print(f"Job type: {self.name}")
    print(f"Salary: ${self.salary}")
    print(f"Hours worked: {self.hoursWorked}")

class doctor(job):
  specialty = None
  yearsExperience = None

  def __init__(self, specialty, yearsExperience):
    self.name = "Doctor"
    self.salary = 250000
    self.hoursWorked = 60
    self.specialty = specialty
    self.yearsExperience = yearsExperience

  def details(self):
    print()
    print(f"Job type: {self.name}")
    print(f"Salary: ${self.salary}")
    print(f"Hours worked: {self.hoursWorked}")
    print(f"Specialty: {self.specialty}")
    print(f"Years of Experience: {self.yearsExperience}")

class teacher(job):
  subject = None
  position = None
  
  def __init__(self, subject, position):
    self.name = "Teacher"
    self.salary = 50000
    self.hoursWorked = "All of them"
    self.subject = subject
    self.position = position

  def details(self):
    print()
    print(f"Job type: {self.name}")
    print(f"Salary: ${self.salary}")
    print(f"Hours worked: {self.hoursWorked}")
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}")

janitor = job("Janitor", 35000, 32)
CSTeacher = teacher("Computer Science", "Classroom Teacher")
emergencyDoctor = ("Emergency Medicine", "4")

print("🌟Jobs Jobs Jobs!🌟")
janitor.details()
CSTeacher.details()
doctor.details()
