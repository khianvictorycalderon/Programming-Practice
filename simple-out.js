const input = require("./input");

// IIFE
(async() => {
    const name = await input("Enter your name: ");
    const age = await input("Enter your age: ");
    console.log(`Hello ${name}, you are ${age} years old.`);
})();