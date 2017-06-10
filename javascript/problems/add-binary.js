/**
 * @since 2017-06-10 14:58:30
 * @author vivaxy
 * @see https://leetcode.com/problems/add-binary/

 Given two binary strings, return their sum (also a binary string).

 For example,
 a = "11"
 b = "1"
 Return "100".

 */

/**
 * @see https://leetcode.com/submissions/detail/105560605/
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    var length = Math.max(a.length, b.length);
    var remaining = 0;
    var index = -1;
    var result = '';
    while (index++ < length - 1) {
        var bit1 = Number(a[a.length - 1 - index] || '0');
        var bit2 = Number(b[b.length - 1 - index] || '0');
        var sum = bit1 + bit2 + remaining;
        remaining = 0;
        if (sum > 1) {
            remaining = 1;
            sum = sum - 2;
        }
        result = String(sum) + result;
    }
    if (remaining) {
        result = 1 + result;
    }
    return result;
};

var test = require('ava');
test('main', function(t) {
    t.is(addBinary('11', '1'), '100');
    t.is(addBinary(
        '10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101',
        '110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011'
    ), '110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000');
});
