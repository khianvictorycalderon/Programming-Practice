const input = require("./input");

(async() => {
    const array = await input("Enter list of array separated by comma:\n");
    let reversedArray = [];

    array.split(",").forEach(item => {
        reversedArray.unshift(item);
    });

    // Reverse array:
    console.log(`Reversed array: \n${reversedArray}`);

})();