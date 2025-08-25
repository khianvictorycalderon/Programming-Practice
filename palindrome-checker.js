const input = require("./input");

(async() => {
    const raw_word = await input("Enter a word (no space): ");
    const word = String(raw_word).toLowerCase();
    
    // Validate first
    if (word.includes(" ")) {
        console.log("I said no space :)");
        return;
    }

    // Make a reversed word
    let reversed = "";
    for (let i = word.length - 1 ; i >= 0 ; i--) {
        reversed += word[i];
    }

    // Check if input is palindrome
    if (word == reversed) {
        console.log(`${word} is a palindrome.`);
    } else {
        console.log(`${word} is not a palindrome.`);
    }
})();