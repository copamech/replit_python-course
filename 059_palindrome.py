def palindrome(value):
  length = len(value)
  if length <= 1:
    return True
  if value[0] != value[-1]:
    return False
  return palindrome(value[1:-1])

print("🌟Palindrome Checker🌟")
print()
word = input("Input a word: ").strip().lower()
result = palindrome(word)
print()
print(f"Palindrome check: {result}")
