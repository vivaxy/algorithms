/**
 * @since 2017-06-10 09:33:59
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/sqrtx/

 Implement int sqrt(int x).

 Compute and return the square root of x.

 */

/**
 * @see https://leetcode.com/submissions/detail/105538419/
 *
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    return Math.floor(Math.sqrt(x));
};

var test = require('ava');
test('main', function(t) {
    t.is(mySqrt(3), 1);
});
