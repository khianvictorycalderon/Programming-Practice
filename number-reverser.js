const input = require("./input");

(async() => {
    let number = 1234;
    let reversed = 0;

    while(number > 0) {
        // Get the last number
        let last_digit = number % 10;

        // Append to first
        reversed = (reversed + last_digit) * 10;

        // Strip the number
        number = Math.floor(number / 10);
    }

    console.log(reversed / 10); // Removes the extra 0

})();