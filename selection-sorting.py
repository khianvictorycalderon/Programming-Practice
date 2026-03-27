numbers = input("Enter numbers (Separated by input): ")
num_list = [int(num) for num in numbers.split(",")]

def getMin(lt):
    # Assume the first number is the highest
    min = lt[0]
    for item in lt:
        if item < min:
            min = item
    return min

sorted_numbers = []
while (len(num_list) > 0):
    minNum = getMin(num_list)
    sorted_numbers.append(minNum)
    num_list.remove(minNum)

print(f"The new updated orders of number are: {", ".join(map(str, sorted_numbers))}")