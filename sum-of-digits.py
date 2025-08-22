numbers = input("Enter list of numbers separated by comma: ")
separated_numbers = numbers.split(",")
converted_numbers = []

# Converting each string number to number
for item in separated_numbers:
    converted_numbers.append(float(item))

# Sum of the entire array
sum = 0
for item in converted_numbers:
    sum += item

# Printing the sum
print(f"Total sum of {numbers} is {sum}")