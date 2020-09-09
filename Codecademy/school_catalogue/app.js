//Let’s put your knowledge of classes to the test by creating a digital school catalog for the New York City Department of Education. The Department of Education wants the catalog to hold quick reference material for each school in the city.

//We need to create classes for primary and high schools. Because these classes share properties and methods, each will inherit from a parent School class. Our parent and three child classes have the following properties, getters, setters, and methods:


//School class: props: name (str), level (str), numberOfStudents (int); getters: all props; setters: numberOfStudents; methods: .quickfacts() and .pickSubstituteTeadcher() (static method)
class School {
    constructor(name, level, numberOfStudents) {
        this._name = name;
        this._level = level;
        this._numberOfStudents = numberOfStudents;
    }

    //some getters
    get name() {
        return this._name;
    }

    get level() {
        return this._level;
    }

    get numberOfStudents() {
        return this._numberOfStudents;
    }

    set numberOfStudents(newNumberOfStudents) {
        if (typeof newNumberOfStudents === "number") {
            this._numberOfStudents = newNumberOfStudents;
        } else {
            console.log('Invalid input: numberOfStudents must be set to a Number')
        }
    }

    //methods
    quickFacts() {
        console.log(`${this.name} educates ${this.numberOfStudents} students at the ${this.level} school level.`)
    }

    static pickSubstituteTeacher(substituteTeachers) {
        const idx = Math.floor(Math.random() * (substituteTeachers.length - 1))
        return substituteTeachers[idx]
    }

}


//Primary class: props: name (str), level (str), numberOfStudents (int), pickupPolicy (str); getters: all props; setters: numberOfStudents; methods: .quickfacts() and .pickSubstituteTeadcher() (static method)
class Primary extends School{
    constructor(name, numberOfStudents, pickupPolicy) {
        super(name, 'primary', numberOfStudents)
        this._pickupPolicy = pickupPolicy;
    }
    
    //some getters
    get pickupPolicy() {
        return this._pickupPolicy;
    }
}
    

//Middle class: props: name (str), level (str), numberOfStudents (int); getters: all props; setters: numberOfStudents; methods: .quickfacts() and .pickSubstituteTeadcher() (static method)
class Middle extends School{
    constructor(name, numberOfStudents) {
        super(name, 'middle', numberOfStudents)
        }
    }


//Primary class: props: name (str), level (str), numberOfStudents (int), sportsTeams (arr); getters: all props; setters: numberOfStudents; methods: .quickfacts() and .pickSubstituteTeadcher() (static method)
class High extends School{
    constructor(name, numberOfStudents, sportsTeams) {
        super(name, 'high', numberOfStudents)
        this._sportsTeams = sportsTeams;
    }
    
    //some getters
    get sportsTeams() {
        this._sportsTeams.forEach(element => console.log(element));
    }
}

const test = new School('Test', 'High School', 2222);

console.log(test.numberOfStudents);

test.numberOfStudents = 5678;
console.log(test.numberOfStudents);

test.quickFacts();

const lorraineHansbury = new Primary('Lorraine Hansbury', 514, 'Students must be picked up by a parent, guardian, or a family member over the age of 13.')

lorraineHansbury.quickFacts()

console.log(School.pickSubstituteTeacher(['Jamal Crawford', 'Lou Williams', 'J.R Smith', 'James Harden', 'Jason Terry', 'Manu Ginobli']))

const alSmith = new High('Al E. Smith', 415, ['Baseball', 'Basketball', 'Volleyball', 'Track and Field'])

alSmith.sportsTeams

