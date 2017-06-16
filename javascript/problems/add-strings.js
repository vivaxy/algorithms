/**
 * @since 2017-06-10 14:08:59
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/add-strings/

 Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

 Note:

 The length of both num1 and num2 is < 5100.
 Both num1 and num2 contains only digits 0-9.
 Both num1 and num2 does not contain any leading zero.
 You must not use any built-in BigInteger library or convert the inputs to integer directly.

 */

/**
 * @see https://leetcode.com/submissions/detail/105557949/
 *
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    var count = Math.max(num1.length, num2.length);
    var index = 0;
    var result = '';
    var remaining = 0;
    while (index++ < count) {
        var digital1 = Number(num1[num1.length - index] || '0');
        var digital2 = Number(num2[num2.length - index] || '0');
        var sum = digital1 + digital2 + remaining;
        remaining = sum > 9 ? 1 : 0;
        result = String(sum > 9 ? sum - 10 : sum) + result;
    }
    if (remaining) {
        result = String(remaining) + result;
    }
    return result;
};

var test = require('ava');
test('main', function(t) {
    t.is(addStrings('100', '100'), '200');
    t.is(addStrings('9333852702227987', '85731737104263'), '9419584439332250');
    t.is(addStrings('1', '9'), '10');
});
