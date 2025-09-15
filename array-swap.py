items = input("Enter list of array values (number or letter) separated by comma: \n")
swappedIndexes = input("Enter 2 index values you want to switch (separated by comma): \n")
swapIndexesRealNumber = [int(item) for item in swappedIndexes.split(",")]

array = items.split(",")

# Unswapped array
print(f"Input: {array}")

# Perform the swapping
array[swapIndexesRealNumber[0]], array[swapIndexesRealNumber[1]] = array[swapIndexesRealNumber[1]], array[swapIndexesRealNumber[0]]

# Swapped array
print(f"Swapped: {array}")