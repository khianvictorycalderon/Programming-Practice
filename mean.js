const input = require("./input");

(async() => {
    
    const numbers = await input("Enter numbers (Separated by Comma): ");
    const num_list = numbers.replace(" ", "").split(",");
    const num_length = num_list.length;

    let sum = 0;

    // Total sum of all numbers
    num_list.forEach(number => sum += Number(number));

    // Get the average
    const result = sum / num_length;

    console.log(`The mean of ${num_list.join(", ")} is ${result}`);

})();