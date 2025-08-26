import re

sentence = input("Enter a sentence: \n")

words = re.findall(r"\w+", sentence)

word_count = len(words)

print(f"There are {word_count} words in that sentence.")