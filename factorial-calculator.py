# Input
number = int(input("Enter the number for calculating factorial: "))

# Initial value
result = 1

# Calculating the result
for i in range(number, 1, -1):
    result *= i

# Displaying final answer
print(f"{number}! = {result}")