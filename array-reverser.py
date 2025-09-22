array = input("Enter list of array separated by comma:\n")
reversed_array = []

for item in array.split(","):
    reversed_array.insert(0, item)

# Reversed array:
print(f"Reversed array: \n{reversed_array}")