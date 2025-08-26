const input = require("./input");

(async() => {
    const sentence = await input("Enter a sentence: \n");

    let word_count = sentence.replace(/[0-9]/g, "").split(/\s/).length;

    console.log(`There are ${word_count} words in that sentence.`);
})();