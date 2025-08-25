const input = require("./input");

(async() => {
    const number = await input("Enter the number for calculating factorial: ");

    // Initial value
    let result = 1;

    // Calculating the result
    for (let i = Number(number); i > 1; i--) {
        result *= i;
    }

    // Displaying final answer
    console.log(`${number}! = ${result}`);
})();