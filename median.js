const input = require("./input");

function selectionSort(arr) {

    // Make original copy
    const origCopy = [...arr];
    const sortedArray = [];

    function geMin(arr) {
        // Assume the first number is the highest:
        let maxNum = arr[0];
        arr.forEach(item => {
            if (item < maxNum) maxNum = item;
        });
        return maxNum;
    }

    while (origCopy.length > 0) {
        const smallestNumber = geMin(origCopy);
        sortedArray.push(smallestNumber);
        const index = origCopy.indexOf(smallestNumber);
        if (index > -1) origCopy.splice(index, 1);
    }

    return sortedArray;
}

(async() => {
    
    const numbers = await input("Enter numbers (Separated by Comma): ");
    const num_list = numbers.split(",").map(Number);

    // Sort first
    const sorted_list = selectionSort(num_list);

    // Get the middle
    let middle;
    if (sorted_list.length % 2 === 0) {
        const mid1 = Math.floor(sorted_list.length / 2 - 1);
        const mid2 = Math.floor(sorted_list.length / 2);
        middle = [sorted_list[mid1], sorted_list[mid2]];
    } else {
        const mid = Math.floor(sorted_list.length / 2);
        middle = [sorted_list[mid]];
    }

    console.log(`The median is/are: ${middle.join(", ")}`);

})();