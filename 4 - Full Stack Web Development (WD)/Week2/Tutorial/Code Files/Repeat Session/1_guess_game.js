console.log('To stop anytime, enter: q');
let score = 0;

num = Math.floor((Math.random()*11));  // 3.5 -> 3, 3.99 -> 3
let guess = prompt("Guess a number between 0 to 10: ");

while(guess != 'q'){
    guess_num = Number(guess)
    if (guess_num == num){
        console.log('CONGRATS, you guessed it correctly')
        score += 10
        console.log('Your new score:', score)
    }
    else{
        console.log('Your guess did not match')
        console.log('The number was:', num)
    }

    num = Math.floor((Math.random()*11));  // 3.5 -> 3, 3.99 -> 3
    guess = prompt("Guess a number between 0 to 10: ");
}

console.log('Game Over.');

