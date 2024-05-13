//  This covers everything
// for, while, arrays, maps, if's


// Define a set of maps containing information about vehicles, phones, drinks, and programming languages.
let vehicles = [{"Make": "Rolls Royce", "Model": "Phantom", "Year": 2024},
            {"Make": "Range Rover", "Model": "Evoque" ,"Year": 2018},
            {"Make": "Jaguar", "Model": "XJ", "Year": 2016}];
let phones = [{"brand": "Nokia", "type": "3310"}, 
          {"brand": "Motorola", "type": "RazR"}];
let drinks = [{"type": "water", "type": "juice"}];
let programming_languages = ["java"];

// Create a map to associate words with corresponding sets of information.
let bags_of_words = new Map([
    ["car", vehicles],
    ["want", "you intend to buy a"],
    ["phone", phones],
    ["coding", programming_languages],
    ["thirsty", drinks]
]);

// Prompt the user to input a sentence.
let input_sentence = prompt("Write a short sentence here");

// Initialize an array to store the words forming the reply sentence.
let replying_sentence = [];

// Iterate through each word in the input sentence.
for (let word of input_sentence.split(" ")) {
    // Check if the word exists in the bags_of_words map.
    if (bags_of_words.get(word)) {
        // If the value associated with the word is an array, randomly select an item from it.
        if (bags_of_words.get(word) instanceof Array) {
            let word_set_length = bags_of_words.get(word).length;
            let intents = bags_of_words.get(word)[Math.floor(Math.random() * word_set_length)];
            // Display the randomly selected item in the console.
            console.log(bags_of_words.get(word)[Math.floor(Math.random() * word_set_length)]);
            // Append the properties of the selected item to the replying_sentence array.
            for (var val in intents) {
                replying_sentence.push(intents[val]);
            }
        } else {
            // If the value associated with the word is not an array, simply append it to the reply sentence.
            replying_sentence.push(bags_of_words.get(word));
        }
    }
}

// Display the reply sentence to the user.
alert(replying_sentence.join(" "));
