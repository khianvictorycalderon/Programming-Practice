numbers = input("Enter integers (Separated by Comma): ")
num_list = numbers.replace(" ", "").split(",")
num_length = len(num_list)

sum = 0

# Sum of all inputs
for item in num_list:
    sum += int(item)

# Get the average
result = sum / num_length

print(f"The mean of {", ".join(num_list)} is {result}")