import sys
word = input("Enter a word (no space): ").lower()

# Validate first
if " " in word:
    sys.exit("I said no space :)")