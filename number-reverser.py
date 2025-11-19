number = 4321
reversed = 0

# Step by step algorithm
# 0 : 12345
# 5 : 1234
# 54 : 123
# 543 : 12
# 5432 : 1
# 54321 : 0

while number > 0:
    # Get the last digit
    last_digit = number % 10

    # Append as always the first number
    reversed = (reversed + last_digit) * 10

    # Strip the last number on the right
    number //= 10

reversed // 10 # Removes the 0 in the last:
print(reversed // 10)

# Tries:
# last_digit = number % 10
# print(last_digit)

# last_digit = last_digit * 10 + (number // 10) % 10
# print(last_digit)