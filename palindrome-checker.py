import sys
word = input("Enter a word (no space): ").lower()

# Validate first
if " " in word:
    sys.exit("I said no space :)")

# Make a reversed word
reversed = ""
for i in range(len(word) -1, -1, -1):
    reversed += word[i]

# Check if input is palindrome
if word == reversed:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")