/**
 * @since 2017-06-15 19:49:21
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/sum-of-two-integers/

 Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

 Example:
 Given a = 1 and b = 2, return 3.

 */

/**
 * @see https://leetcode.com/submissions/detail/106141491/
 *
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    return a + b;
};

var test = require('ava');
test('main', function(t) {
    t.is(getSum(1, 2), 3);
});
