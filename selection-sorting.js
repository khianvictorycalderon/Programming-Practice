const input = require("./input");

(async() => {

    const numbers = await input("Enter numbers (Separated by input): ");
    const num_list = numbers.replace(/\s/g, "").split(",").map(Number);

    function geMin(arr) {
        // Assume the first number is the highest:
        let maxNum = arr[0];
        arr.forEach(item => {
            if (item < maxNum) maxNum = item;
        });
        return maxNum;
    }

    const sortedArray = [];
    while (num_list.length > 0) {
        const smallestNumber = geMin(num_list);
        sortedArray.push(smallestNumber);
        const index = num_list.indexOf(smallestNumber);
        if (index > -1) num_list.splice(index, 1);
    }

    console.log(`The new updated orders of number are: ${sortedArray.join(", ")}`);

})();