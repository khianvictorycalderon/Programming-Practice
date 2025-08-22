numbers = input("Enter list of numbers separated by comma: ")
converted_numbers = [float(item.strip()) for item in numbers.split(",")]

# Min and Max variable
min_num = converted_numbers[0] # Assuming the first index is the smallest
max_num = converted_numbers[0] # Assuming the first index is the biggest

# Finding both the smallest and biggest number
for item in converted_numbers:
    if item < min_num:
        min_num = item
    if item > max_num:
        max_num = item

# Printing the output
print(f"Smallest (Min) Number: {min_num}\nBiggest (Max) Number: {max_num}")