console.log('To stop anytime, enter: q');
let score = 0;
let guess = 0;
while(true){
    num = Math.floor(Math.random()*11)
    guess = prompt("Guess a number between 0 to 10: ")
    if(guess == 'q'){
        console.log('Game Over.')
        break
    }

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

}
