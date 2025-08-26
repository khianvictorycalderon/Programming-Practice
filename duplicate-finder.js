const input = require("./input");

(async() => {
    const array_set = (await input("Enter values separated by comma: \n")).split(",");
    
    // Set for detecting duplicates
    let seen = new Set();
    let duplicates = new Set();

    // Each element in array
    for (let value of array_set) {
        value = value.trim();
        if (seen.has(value)) {
            duplicates.add(value);
        } else {
            seen.add(value);
        }
    }

    if (duplicates.size > 0) {
        console.log(`The duplicates are the: \n${[...duplicates]}`);
    } else {
        console.log("There are no duplicates in the set.");
    }

})();