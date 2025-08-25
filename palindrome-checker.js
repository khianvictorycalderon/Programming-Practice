const input = require("./input");

(async() => {
    const raw_word = await input("Enter a word (no space): ");
    const word = String(raw_word).toLowerCase();
    
    // Validate first
    if (word.includes(" ")) {
        console.log("I said no space :)");
        return;
    }

    console.log(word);
})();