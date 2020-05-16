//provided by codecademy
let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];

//popping off last value in the array
secretMessage.pop();

console.log(secretMessage.length);

secretMessage.push('to');

secretMessage.push('program');

//changing 'easily' to 'right'
secretMessage[secretMessage.indexOf('easily')] = 'right';

console.log(secretMessage);

//removing first item of secretMessage
secretMessage.shift();

//adding Programming to the beginning of the list
secretMessage.unshift('Programming');

//splicing out get, right, the, first, time and replacing it with 'know'
secretMessage.splice(secretMessage.indexOf('get'), 5, 'know');

console.log(secretMessage);

// joining strings into one sentence
console.log(secretMessage.join(' '));

