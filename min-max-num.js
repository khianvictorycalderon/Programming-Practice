const input = require("./input");

(async() => {
    const numbers = await input("Enter list of numbers separated by comma: ");
    const converted_numbers = numbers.split(",").map(item => Number(item.trim()));

    // Min and Max variable
    min_num = converted_numbers[0]; // Assuming the first index is the smallest
    max_num = converted_numbers[0]; // Assuming the first index is the biggest

    // Finding both the smallest and biggest number
    converted_numbers.forEach((item, index) => {
        if (item < min_num) min_num = converted_numbers[index];
        if (item > max_num) max_num = converted_numbers[index];
    });

    // Printing the output
    console.log(`Smallest (Min) Number: ${min_num}\nBiggest (Max) Number: ${max_num}`);

})();