const input = require("./input");

(async () => {
    const numbers = await input("Enter numbers (Separated by Comma): ");
    const num_list = numbers.split(",").map(Number);

    // Count occurrences
    let instancesCount = {};
    num_list.forEach(num => {
        if (instancesCount[num]) {
            instancesCount[num] += 1;
        } else {
            instancesCount[num] = 1;
        }
    });

    // Display counts
    console.log("Count of all numbers:");
    for (let [num, count] of Object.entries(instancesCount)) {
        console.log(`${num}: ${count}`);
    }

    // Find the max count
    let maxCount = 0;
    for (let num in instancesCount) {
        if (instancesCount[num] > maxCount) {
            maxCount = instancesCount[num];
        }
    }

    // Collect all modes
    let modes = [];
    for (let num in instancesCount) {
        if (instancesCount[num] === maxCount) {
            modes[modes.length] = num; // push manually
        }
    }

    console.log(`Mode(s): ${modes.join(", ")}`);
})();