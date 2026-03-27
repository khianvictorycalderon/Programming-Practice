# Get input from the user
numbers = input("Enter numbers (Separated by Comma): ")
num_list = [int(num) for num in numbers.split(",")]

# Count occurrences
instances_count = {}
for num in num_list:
    if num in instances_count:
        instances_count[num] += 1
    else:
        instances_count[num] = 1

# Display counts
print("Count of all numbers:")
for num, count in instances_count.items():
    print(f"{num}: {count}")

# Find the max count manually
max_count = 0
for count in instances_count.values():
    if count > max_count:
        max_count = count

# Collect all modes
modes = []
for num, count in instances_count.items():
    if count == max_count:
        modes.append(str(num))  # convert to string for printing

print(f"Mode(s): {', '.join(modes)}")