/**
 * @since 2017-06-10 17:09:33
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/plus-one/

 Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

 You may assume the integer do not contain any leading zero, except the number 0 itself.

 The digits are stored such that the most significant digit is at the head of the list.

 */

/**
 * @see https://leetcode.com/submissions/detail/105567401/
 *
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    var remaining = 1;
    for (var i = digits.length - 1; i >= 0; i--) {
        var value = digits[i] + remaining;
        if (value >= 10) {
            digits[i] = 0;
            remaining = 1;
        } else {
            remaining = 0;
            digits[i] = value;
        }
    }
    if (remaining) {
        digits.unshift(1);
    }
    return digits;
};

var test = require('ava');
test('main', function(t) {
    t.deepEqual(plusOne([9]), [1, 0]);
});
