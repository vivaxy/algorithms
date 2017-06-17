/**
 * @since 2017-06-17 09:07:32
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/add-digits/

 Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

 For example:

 Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

 Follow up:
 Could you do it without any loop/recursion in O(1) runtime?

 */

/**
 * @see https://leetcode.com/submissions/detail/106303296/
 *
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    var numAsString = String(num);
    if (numAsString.length === 1) {
        return num;
    }
    return addDigits(numAsString.split('').reduce(function(acc, cur) {
        return acc + Number(cur);
    }, 0));
};

/**
 * @see https://leetcode.com/submissions/detail/106303586/
 *
 * @param {number} num
 * @return {number}
 */
var addDigits2 = function(num) {
    return (num - 1) % 9 + 1;
};

var test = require('ava');
test('main', function(t) {
    t.is(addDigits(38), 2);

    t.is(addDigits2(38), 2);
});
