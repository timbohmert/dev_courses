//Functions to play rock paper scissors that will 1. get the user's choice 2. get the computer's choice 3. Compare the two choices and determine a winner 4. start the program and display the results
//Creating function for determining the User's Choice of rock, paper, or scissors
const getUserChoice = userInput => {
    userInput.toLowerCase();
    if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') { 
        return userInput;
    } else console.log('Inccorect entry. Please enter rock, paper, or scissors.');
};

//Creating function for determining the Computer's choice of rock, paper, or scissors
const getComputerChoice = () => {
    i = Math.floor(Math.random()*3)
    if (i == 0) {
        return 'rock'
    } else if (i == 1) {
        return 'scissors'
    } else if (i == 2) {
        return 'paper'
    } else return 'Error'
}

//creating function to determine winner between the computer and the user
const determineWinner = (userChoice, computerChoice) => {
    if (userChoice === computerChoice) {
        return 'The game was a tie';
    } else if (userChoice === 'bomb') {
        return 'Total destruction! You dominated your opponent!'
    } else if ((userChoice === 'rock' && computerChoice === 'scissors') || (userChoice === 'paper' && computerChoice === 'rock') || (userChoice === 'scissors' && computerChoice === 'paper')) {
        return "Yay! You won!"
    } else if ((computerChoice === 'rock' && userChoice === 'scissors') || (computerChoice === 'paper' && userChoice === 'rock') || (computerChoice === 'scissors' && userChoice === 'paper')) {
        return "Rats! You were defeated!"
    } else return 'Error in your entry.'
}

//Start game and log results
const playGame = user => {
    userChoice = getUserChoice(user);
    computerChoice = getComputerChoice();
    console.log(userChoice, computerChoice);
    console.log(determineWinner(userChoice, computerChoice))
}