def selectionSort(arr):

    origCopy = arr.copy()
    sorted_numbers = []

    def getMin(lt):
        # Assume the first number is the highest
        min = lt[0]
        for item in lt:
            if item < min:
                min = item
        return min
    
    while (len(origCopy) > 0):
        minNum = getMin(origCopy)
        sorted_numbers.append(minNum)
        origCopy.remove(minNum)

    return sorted_numbers

numbers = input("Enter numbers (Separated by input): ")
num_list = [int(num) for num in numbers.split(",")]

# Sort first
sorted_list = selectionSort(num_list)

# Get the middle
if (len(sorted_list) % 2 == 0):
    mid1 = len(sorted_list) // 2 - 1
    mid2 = len(sorted_list) // 2
    middle = [sorted_list[mid1], sorted_list[mid2]]
else:
    middle = [sorted_list[len(sorted_list) // 2]]

print(f"he median is/are: {", ".join(map(str, middle))}")