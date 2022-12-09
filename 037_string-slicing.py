print("🌟Star Wars Name Generator🌟")
print()
firstName = input("First name: ").strip().capitalize()
print()
lastName = input("Last name: ").strip().lower()
print()
maidenName = input("Mother's maiden name: ").strip().capitalize()
print()
birthplace = input("City where you were born: ").strip().lower()
print()

sliceOne = firstName[:3]
sliceTwo = lastName[:3]
sliceThree = maidenName[:2]
sliceFour = birthplace[-3:]

SWName = f"{sliceOne}{sliceTwo} {sliceThree}{sliceFour}"

print(f"Your Star Wars name is {SWName}")
