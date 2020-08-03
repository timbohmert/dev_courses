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

    //words method. splits string into array of words
    words(str) {
        words = str.split(' ')
        return words
    },

    //.pad() method 
    pad(str, length) {
        pad = length - str.length
        while (pad > 0) {
            if  (pad > 1) {
                str = ' ' + str + ' ';
                pad -= 2;
            } else {
                str = str + ' ';
                pad -= 1;
            }
        } return str;
    },

    //.has() method to check if key has value as direct property of object
    has(obj, key) {
        return obj[key] !== undefined;
    },

    //.invert() method creates array object composed of inverted keys and values of object
    invert(obj) {
        new_obj = {};
        for (const old_key in obj) {
            new_key = obj[old_key];
            new_obj[new_key] = old_key;
        } return new_obj;
    },

    //.findKey() method returns key of first element predicate returns truthy for - predicate is function that returns boolean
    findKey(obj, predicate) {
        for (key in obj) {
            value = obj[key]; 
            if (predicate(value)) {
                return key;
            }
        }
    },

    //.drop() method creates slice of array with n elements dropped from beginning
    drop(arr, n = 1) {
        return arr.slice(n, arr.length);
    },

    //.dropWhile() method creates slice of array excluding elements dropped from beginning. elements are dropped until predicate returns falsey
    dropWhile(arr, predicate) {
        i = 0
        while (predicate(arr[i], i, arr)) {
            i++;
        } return this.drop(arr, i);
    },

    //.chunk() method creates array of elements split into groups the length of size, if can't split evenly, final chunk will be remaining elements
    chunk(arr, n = 1) {
        new_arr = [];
        for (i=0; i < arr.length; i += n) {
            new_arr.push(arr.slice(i, i + n));
        } return new_arr;
    }

};






// Do not write or modify code below this line.
module.exports = _;

console.log(_.words('Hello my name is tim.'))