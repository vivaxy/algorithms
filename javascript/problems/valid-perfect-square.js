/**
 * @since 2017-06-10 17:05:01
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/valid-perfect-square/

 Given a positive integer num, write a function which returns True if num is a perfect square else False.

 Note: Do not use any built-in library function such as sqrt.

 Example 1:

 Input: 16
 Returns: True
 Example 2:

 Input: 14
 Returns: False

 */

/**
 * @see https://leetcode.com/submissions/detail/105567135/
 *
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    var sqrt = Math.sqrt(num);
    return sqrt === Math.floor(sqrt);
};

var test = require('ava');
test('main', function(t) {
    t.is(isPerfectSquare(16), true);
    t.is(isPerfectSquare(14), false);
});
