/*Goal (provided by Codecademy):

In this project, you will use what you know about iterating over arrays to improve the quality of a paragraph and gather some information about that paragraph.

This is the same type of work that word processing software does. Additionally, you may have heard of linting, a process by which text is evaluated and improved by an application. In this project, you will create a miniature version of a linter using array methods that you have learned.*/


//story, overusedWords, and unnecessaryWords provided by Codecademy
let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.';

let overusedWords = ['really', 'very', 'basically'];

let unnecessaryWords = ['extremely', 'literally', 'actually' ];

//converting story into array of all of the words

//splits story string into individual words and puts in storyWords array
storyWords = story.split(' ');

//prints to the log the length of the storyWords array
console.log(storyWords.length);

//creates array with filtered out unnecessaryWords from the storyWords
const betterWords = storyWords.filter(x => !(unnecessaryWords.includes(x)));


//function counts occurence of each word in overusedWords
const overusedWord_count = () => {
    let overusedWord_string = ''
    overusedWords.forEach( x => {
        let wordCount = 0;
        for (let i = 0; i < storyWords.length; i++) {
            if (x == storyWords[i]) {
                wordCount++;
            };
        } overusedWord_string += `The word \"${x}\" was used ${String(wordCount)} time(s).\n`;
        
    }); return overusedWord_string
};

//function counts the occurrence of (.) or (!) to then count the number of sentences in the story phrase
const sentCount = () =>{
    let count = 0;
    storyWords.forEach(x => {
        if (x.includes('.') || x.includes('!')) {
            count++;
        }; 
    }); return count;
};
console.log(sentCount);

//logs the word count, sentence count, and number of times each overused word appears
const log_info = () => {
    console.log(`The word count is ${storyWords.length}.\n`, `The sentence count is ${sentCount()}.\n`, overusedWord_count());
};

log_info()

//joings the words from array of betterWords into one string
console.log(betterWords.join(' '))