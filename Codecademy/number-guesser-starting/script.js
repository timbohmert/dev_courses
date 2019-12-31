let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

//function to create random number between 0 and 9
const generateTarget = () => Math.floor(Math.random() * 10);

//function to compare computer and user guess
const getAbsoluteDistance = (guess, targ) => Math.abs(guess - targ);

const compareGuesses = (human, computer, target) => getAbsoluteDistance(human, target) <= getAbsoluteDistance(computer, target);

//update the overall score between the user and the computer
const updateScore = (str) => str === 'human' ? humanScore++ : computerScore++;

//advance the round
const advanceRound = () => currentRoundNumber++;