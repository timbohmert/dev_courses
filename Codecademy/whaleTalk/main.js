/* Project task and goals:

Take a phrase like ‘turpentine and turtles’ and translate it into its “whale talk” equivalent: ‘UUEEIEEAUUEE’.

There are a few simple rules for translating text to whale language:

There are no consonants. Only vowels excluding “y”.
The u‘s and e‘s are extra long, so we must double them in our program.
Once we have converted text to the whale language, the result is sung slowly, as is a custom in the ocean.

To accomplish this translation, we can use our knowledge of loops. Let’s get started! */

//input string that will be transplated into whale talk
let input = 'happy birthday wesson, you are the best';

//list containing all vowels
const vowels = ['a', 'e', 'i', 'o', 'u'];

//array that will be populated with vowels from input string
let resultArray = [];

for (i = 0; i < input.length; i++) {   
    //console.log(i)
    for (j = 0; j < vowels.length; j++) {
        console.log(j);
        if (input[i] === vowels[j]) {
            resultArray.push(input[i]);
            if (input[i] === 'e' || input[i] === 'u') {
                resultArray.push(input[i]);
            }
        }
    }
}

console.log(resultArray);

console.log(resultArray.join('').toUpperCase());


