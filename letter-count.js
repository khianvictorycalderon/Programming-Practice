const input = require("./input");

const consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"];
const vowels = ["A", "E", "I", "O", "U"];

(async() => {
    const sentence = await input("Enter sentence input: ");
    
    // Count variables
    let vowels_count = 0;
    let consonants_count = 0;

    // Counting consonants and vowels
    sentence.toUpperCase().split("").forEach(item => {
        if (consonants.includes(item)) consonants_count += 1;
        if (vowels.includes(item)) vowels_count += 1;
    });

    // Printing the output
    console.log(`Total Vowel/s: ${vowels_count}\nTotal Consonant/s: ${consonants_count}`);
})();