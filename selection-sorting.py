numbers = input("Enter numbers (Separated by input): ")
num_list = [int(num) for num in numbers.split(",")]

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

print(f"The new updated orders of number are: {", ".join(map(str, selectionSort(num_list)))}")