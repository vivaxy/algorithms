/**
 * @since 2017-06-10 13:46:27
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/reverse-bits/

 Reverse bits of a given 32 bits unsigned integer.

 For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

 Follow up:
 If this function is called many times, how would you optimize it?

 Related problem: Reverse Integer

 */

/**
 * @see https://leetcode.com/submissions/detail/105555113/
 *
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    var bits = n.toString(2).split('');
    var imp = 32 - bits.length;
    while (imp--) {
        bits.unshift('0');
    }
    return parseInt(bits.reverse().join(''), 2);
};

var test = require('ava');
test('main', function(t) {
    t.is(reverseBits(43261596), 964176192);
});
