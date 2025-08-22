sentence = input("Enter sentence input: ")

consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vowels = ["A", "E", "I", "O", "U"]

# Count variables
consonants_count = 0
vowels_count = 0

# Counting consonants and vowels
for item in sentence.upper():
    if item in consonants:
        consonants_count += 1
    if item in vowels:
        vowels_count += 1

# Printing the output
print(f"Total Vowel/s: {vowels_count}\nTotal Consonant/s: {consonants_count}")