/* Goal (provided by Codecademy): In this project, you will be implementing some of the most exciting functionality from the widely-popular lodash.js library. You will be implementing ten methods that add new functionality for numbers, strings, objects, and arrays.

In implementing each method, we will follow these four steps:

Specify the functionality of the method we are implementing
Ideate a game plan for how to implement this functionality in code
Implement our game plan
Test our code to ensure it works as expected

We encourage you to try to complete the “Ideate” and “Implement” steps on your own before consulting our suggestions for each. It may be difficult at points, but working through difficult problems on your own will be incredibly helpful in your journey to become a stronger developer. Once you’ve come up with a solution on your own, or if you have become so stuck you are no longer being productive, check out our steps to see our suggestions for how to solve the problem.

There is no right or wrong answer when it comes to programming. As a result, don’t be frustrated if the solution we present is different than the solution you came up with. We are merely trying to challenge you to consider many different solutions. Your solution is equally as valid as ours. Consider the one you were going to write and then consider ours. Whichever you pick in the end is completely your decision, and we support it completely. */


const _ = {

    //clamp method
    clamp(num, lower, upper) {
        if (num < lower) {
            return lower;
        } else if (num > upper) {
            return upper
        } else {
            return num
        };
    },

    //inRange method
    inRange(num, num_2, num_3 = 0) {
        let start = Math.min(num_2, num_3);
        let end = Math.max(num_2, num_3);
        return start <= num && num < end;
    },

    //words method. For loops 
    words(str) {

    },

    //.pad() method 
    pad(str, length) {

    },

    //
};






// Do not write or modify code below this line.
module.exports = _;