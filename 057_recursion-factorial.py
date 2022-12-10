def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value-1)

answer = 0
print("🌟Factorial Finder🌟")
print()
number = int(input("Input a number: "))
print()

answer = factorial(number)

print(f"The factorial of {number} is {answer}.")
