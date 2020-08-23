/*
Build a Library
Congratulations, you’ve passed the grueling rigmarole of librarian school and have become head librarian at your local Books-‘N-Stuff.

Just as you sit down, eager to utilize all those skills you learned in “Lib 203 - Shushing: How to Maintain Order While Spitting”, you realize you’re still using index cards to handle everything.

But no matter, you know some JavaScript, so let’s get to work modernizing your new digs.

Books-‘N-Stuff carries three different types of media: books, CDs, and movies. In this project you will create a parent class named Media with three subclasses: Book, Movie, and CD. These three subclasses have the following properties and methods:

Book
Properties: author (string), title (string), pages (number), isCheckedOut (boolean, initially false), and ratings (array, initially empty).
Getters: all properties have a getter
Methods: .getAverageRating(), .toggleCheckOutStatus(), and .addRating()
Movie
Properties: director (string), title (string), runTime (number), isCheckedOut (boolean, initially false), and ratings (array, initially empty)
Getters: all properties have a getter
Methods: .getAverageRating(), .toggleCheckOutStatus(), and .addRating()
CD
Properties: artist (string), title (string), isCheckedOut (boolean, initially false), and ratings (array, initially empty), songs (array of strings)
Getters: all properties have a getter
Methods: .getAverageRating(), .toggleCheckOutStatus(), and .addRating()
*/

//parent library - Media
class Media {
    
    //constructor with title that should take string, isCheckedOut set to false, and ratings with empty arr
    constructor(title) {
        this._title = title;
        this._isCheckedOut = false;
        this._ratings =[];
    }

    //parent getters
    get title() {
        return this._title;
    }

    get isCheckedOut() {
        return this._isCheckedOut;
    }

    get ratings() {
        return this._ratings;
    }

    set isCheckedOut(newStatus) {
        this._isCheckedOut = newStatus;
    }

    //method to return average rating
    getAvgRatings() {
        let sum = this._ratings.reduce((currentSum, x) => x + currentSum, 0);
        return sum/this._ratings.length;
    }
    
    //method to toggle the checkedOutStatus
    toggleCheckOutStatus() {
        this._isCheckedOut = !this._isCheckedOut;
    }
    
    //method to add rating to the ratings arr
    addRating(rating) {
        this._ratings.push(rating);
    }
}


//book class that will inherit Media class add author (string) and pages (int) to instance variables
class Book extends Media {
    constructor(title, author, pages) {
        super(title)
        this._author = author;
        this._pages = pages;
    }

    //some getters
    get author() {
        return this._author;
    }

    get pages() {
        return this._pages;
    }
}

//movie class that will inherit Media class add director (string) and runTime (int) to instance variables
class Movie extends Media {
    constructor(title, director, runTime) {
        super(title)
        this._director = director;
        this._runTime = runTime;
    }

    //some getters
    get director() {
        return this._director;
    }

    get runTime() {
        return this._runTime;
    }
}

//CD class that will inherit Media class add artist (string) and songs (arr) to instance variables
class CD extends Media {
    constructor(title, artist, songs) {
        super(title)
        this._artist = artist;
        this._songs = songs;
    }

    //some getters
    get artist() {
        return this._artist;
    }

    get songs() {
        return this._songs;
    }
}


//instances

const historyOfEverything = new Book('A Short History of Nearly Everything', 'Bill Bryson', 554);

historyOfEverything.toggleCheckOutStatus();

console.log(historyOfEverything.isCheckedOut)

historyOfEverything.addRating(4)
historyOfEverything.addRating(5)
historyOfEverything.addRating(5)

console.log(historyOfEverything.getAvgRatings())

const speed = new Movie('Speed', 'Jan de Bont', 116)

speed.toggleCheckOutStatus()

console.log(speed.isCheckedOut)

speed.addRating(1)
speed.addRating(1)
speed.addRating(5)

console.log(speed.getAvgRatings())