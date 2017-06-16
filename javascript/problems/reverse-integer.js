/**
 * @since 2017-06-09 18:50:52
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/reverse-integer/

 Reverse digits of an integer.

 Example1: x = 123, return 321
 Example2: x = -123, return -321

 click to show spoilers.

 Note:
 The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

 */

/**
 * @see https://leetcode.com/submissions/detail/105485452/
 *
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var result;
    if (x < 0) {
        result = -Number(String(-x).split('').reverse().join(''));
    } else {
        result = Number(String(x).split('').reverse().join(''));
    }
    if (result > Math.pow(2, 31)) {
        return 0;
    }
    if (result < -Math.pow(2, 31)) {
        return 0;
    }
    return result;
};

/**
 * @see https://leetcode.com/submissions/detail/105485673/
 *
 * @param {number} x
 * @return {number}
 */
var reverse2 = function(x) {
    var result = 0;
    while (x) {
        result = result * 10 + x % 10;
        x = parseInt(x / 10);
    }
    if (result > 2147483647 || result < -2147483647) {
        return 0;
    }
    return result;
};

var test = require('ava');
test('main', function(t) {
    t.is(reverse(123), 321);
    t.is(reverse(-123), -321);
    t.is(reverse(1534236469), 0);
    t.is(reverse(-2147483648), 0);
    t.is(reverse(-2147483412), -2143847412);
    t.is(reverse(1463847412), 2147483641);

    t.is(reverse2(123), 321);
    t.is(reverse2(-123), -321);
    t.is(reverse2(1534236469), 0);
    t.is(reverse2(-2147483648), 0);
    t.is(reverse2(-2147483412), -2143847412);
    t.is(reverse2(1463847412), 2147483641);
});
