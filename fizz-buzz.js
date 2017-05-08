/**
 * @since 2017-05-08 09:53:00
 * @author vivaxy
 * @see https://leetcode.com/problems/fizz-buzz/

 Write a program that outputs the string representation of numbers from 1 to n.

 But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

 Example:

 n = 15,

 Return:
 [
 "1",
 "2",
 "Fizz",
 "4",
 "Buzz",
 "Fizz",
 "7",
 "8",
 "Fizz",
 "Buzz",
 "11",
 "Fizz",
 "13",
 "14",
 "FizzBuzz"
 ]

 */

/**
 * @see https://leetcode.com/submissions/detail/102281750/
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var results = [];
    for (var i = 1; i <= n; i++) {
        var fizz = i % 3 === 0;
        var buzz = i % 5 === 0;
        if (fizz && buzz) {
            results.push('FizzBuzz');
        } else if (fizz) {
            results.push('Fizz');
        } else if (buzz) {
            results.push('Buzz');
        } else {
            results.push(String(i));
        }
    }
    return results;
};

var expect = require('./lib').expect;
var isSameArray = require('./lib').isSameArray;
expect(isSameArray(fizzBuzz(15), [
    '1',
    '2',
    'Fizz',
    '4',
    'Buzz',
    'Fizz',
    '7',
    '8',
    'Fizz',
    'Buzz',
    '11',
    'Fizz',
    '13',
    '14',
    'FizzBuzz'
]), true);
expect(isSameArray(fizzBuzz(1), ['1']), true);
