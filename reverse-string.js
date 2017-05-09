/**
 * @since 2017-05-09 09:53:57
 * @author vivaxy
 * @see https://leetcode.com/problems/reverse-string/

 Write a function that takes a string as input and returns the string reversed.

 Example:
 Given s = "hello", return "olleh".

 */

/**
 * @see https://leetcode.com/submissions/detail/102380518/
 * @param {string} s
 * @return {string}
 */
var reverseString = function(s) {
    return s.split('').reverse().join('');
};

var expect = require('./lib').expect;
expect(reverseString('hello'), 'olleh');
