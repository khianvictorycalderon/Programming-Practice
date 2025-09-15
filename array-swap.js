const input = require("./input");

(async() => {

    const items = await input("Enter list of array values (number or letter) separated by comma: \n");
    const swapIndexes = await input("Enter 2 index values you want to switch (separated by comma): \n");
    const swapIndexesRealNumber = swapIndexes.split(",").map(item => Number(item));

    let array = items.split(",");

    // Unswapped array
    console.log(`Input: ${array}`);
    
    // Perform the swapping
    [array[swapIndexesRealNumber[0]], array[swapIndexesRealNumber[1]]] = [array[swapIndexesRealNumber[1]], array[swapIndexesRealNumber[0]]]

    // Swapped array
    console.log(`Swapped: ${array}`);

})();