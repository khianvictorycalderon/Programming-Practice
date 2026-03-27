const input = require("./input");

(async() => {

    const numbers = await input("Enter numbers (Separated by input): ");
    const num_list = numbers.replace(/\s/g, "").split(",").map(Number);

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

    console.log(`The new updated orders of number are: ${selectionSort(num_list).join(", ")}`);

})();