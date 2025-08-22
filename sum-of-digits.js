const input = require("./input");

(async() => {
    const numbers = await input("Enter list of numbers separated by comma: ");
    const separated_numbers = numbers.split(",");
    let converted_numbers = [];
    
    // Converting each number string to number
    separated_numbers.map((item) => {
        converted_numbers.push(parseFloat(item));
    })

    // Sum of the entire array
    let sum = 0;
    converted_numbers.forEach(item => {
        sum += item;
    });
    
    // Printing the sum
    console.log(`Total sum of ${numbers} is ${sum}`);
})();