/* We want to create and extract information about your favorite sports team. Basketball, soccer, tennis, or water polo, you pick it. It’s your job to create data using the JavaScript data structures at your disposal: arrays, objects, etc.

Once created, you can manipulate these data structures as well as gain insights from them. For example, you might want to get the total number of games your team has played, or the average score of all of their games. */


// team object

const team = {

    //dream team roster
    _players: [{firstName: 'Christian', lastName: 'Laettner', age: 22},
        {firstName: 'David', lastName: 'Robinson', age: 26},
        {firstName: 'Patrick', lastName: 'Ewing', age: 29},
        {firstName: 'Larry', lastName: 'Bird', age: 35},
        {firstName: 'Scottie', lastName: 'Pippen', age: 26},
        {firstName: 'Michael', lastName: 'Jordan', age: 29},
        {firstName: 'Clyde', lastName: 'Drexler', age: 30},
        {firstName: 'Karl', lastName: 'Malone', age: 28},
        {firstName: 'John', lastName: 'Stockton', age: 30},
        {firstName: 'Chris', lastName: 'Mullin', age: 28},
        {firstName: 'Charles', lastName: 'Barkley', age: 29},
        {firstName: 'Magic', lastName: 'Johnson', age: 32}],

    //schedule for the dream team
    _games: [{opponents: 'Angola', teamPoints: 116, opponentsPoints: 48},
        {opponents: 'Croatia', teamPoints: 103, opponentsPoints: 70},
        {opponents: 'Germany', teamPoints: 111, opponentsPoints: 68},
        {opponents: 'Brazil', teamPoints: 127, opponentsPoints: 83},
        {opponents: 'Spain', teamPoints: 122, opponentsPoints: 81},
        {opponents: 'Puerto Rico', teamPoints: 115, opponentsPoints: 77},
        {opponents: 'Lithuania', teamPoints: 127, opponentsPoints: 76},
        {opponents: 'Croatia', teamPoints: 117, opponentsPoints: 85}],
    
    get players(){
        return this._players;
    },
    
    get games(){
        return this._games;
    },

    addPlayer(firstName, lastName, age) {
        let new_player = {
            firstName, lastName, age
        };
        this._players.push(new_player);
    },

    addGame(opponents, teamPoints, opponentsPoints) {
        let new_game = {opponents, teamPoints, opponentsPoints
        };
        this._games.push(new_game);
    }
};

team.addPlayer('Steph', 'Curry', 28)
team.addPlayer('Lisa', 'Leslie', 44)
team.addPlayer('Bugs', 'Bunny', 76)

console.log(team.players)

team.addGame('Minnesota Lakers', 140, 80)
team.addGame('Monstars', 110, 109)
team.addGame('Lakeville Youth', 81, 93)

console.log(team.games)