array_set = input("Enter values separated by comma: \n").replace(" ", "").split(",")

# Set for detecting duplicates
seen = set()
duplicate = set()

for item in array_set:
    if item in seen:
        duplicate.add(item)
    else:
        seen.add(item)

if len(duplicate) > 0:
    print(f"The duplicates are the: \n{duplicate}")
else:
    print("There are no duplicates in the set.")