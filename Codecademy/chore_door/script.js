//Your mission is to construct a single-page website that plays a fully-functional game. You will see how HTML, CSS, and JavaScript interact harmoniously to produce a dynamic website.

//global variables for door1, door2, and door3 elements from HTML
let doorImage1 = document.getElementById('door1');
let doorImage2 = document.getElementById('door2');
let doorImage3 = document.getElementById('door3');

//global variables for the different images behind the doors: bot, beach, space and closed door
let botDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/robot.svg';

let beachDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/beach.svg';

let spaceDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/space.svg';

let closedDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/closed_door.svg';

//global variable captures the number of doors currently closed
let numClosedDoors = 3;

//global variables for different doors
let openDoor1;

let openDoor2;

let openDoor3;

//global variables for startButton from HTML
let startButton = document.getElementById('start');

//determines if the user is currently playing a game
let currentlyPlaying = true;


//function to determine if the bot was behind opened door
const isBot = (door) => {
    return door.src ===  botDoorPath;
}


//function to determine if the current door is open or closed
const isClicked = (door) => {
    return door.src !== closedDoorPath;
};


//function for determining number of doors closed and if the user won
const playDoor = (door) => {
    numClosedDoors--;
    if (numClosedDoors === 0) {
        gameOver('win');
    } else if (isBot(door) === true) { 
        gameOver()
    }
};


//function for generating random order of the images behind the doors
const randomChoreDoorGenerator = () => {
    let choreDoor = Math.floor(Math.random() * numClosedDoors);
    if (choreDoor == 1) {
        openDoor1 = botDoorPath;
        openDoor2 = beachDoorPath;
        openDoor3 = spaceDoorPath;
    } else if (choreDoor == 2) {
        openDoor1 = spaceDoorPath;
        openDoor2 = botDoorPath;
        openDoor3 = beachDoorPath;
    } else {
        openDoor1 = beachDoorPath;
        openDoor2 = spaceDoorPath;
        openDoor3 = botDoorPath;
    };
};


//functions for opening doors 1, 2, 3 when clicked on if they are not currently open
doorImage1.onclick = () => {
    if (currentlyPlaying === true && isClicked(doorImage1) !== true) {
        doorImage1.src = openDoor1;
        playDoor(doorImage1);
    };
};

doorImage2.onclick = () => {
    if (currentlyPlaying === true && isClicked(doorImage2) !== true) {
        doorImage2.src = openDoor2;
        playDoor(doorImage2);
    };
};

doorImage3.onclick = () => {
    if (currentlyPlaying === true && isClicked(doorImage3) !== true) {
        doorImage3.src = openDoor3;
        playDoor(doorImage3);
    };
};


//click handler for reseting the page with closed doors and reseting the closed door count
startButton.onclick = () => {
    if (currentlyPlaying === false) {
        startRound();
    }
}


//resets the doors to closed and closed doors to 3 when the start button is clicked
const startRound = () => {
    doorImage1.src  = closedDoorPath;
    doorImage2.src = closedDoorPath;
    doorImage3.src = closedDoorPath;
    numClosedDoors = 3;
    startButton.innerHTML = 'Good luck!';
    currentlyPlaying = true
    randomChoreDoorGenerator();
}


//function that runs when the user has won or lost
const gameOver = (status) => {
    if (status === 'win') {
        startButton.innerHTML = 'You win! Play again?'
    } else {
        startButton.innerHTML = 'Game over! Play again?'
    }
    currentlyPlaying = false
}

//call of startRound() function to allow the user to play the game
startRound()