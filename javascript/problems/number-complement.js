/**
 * @since 2017-05-02 10:11:10
 * @author vivaxy
 * @see https://leetcode.com/problems/number-complement/

 Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 Note:
 The given integer is guaranteed to fit within the range of a 32-bit signed integer.
 You could assume no leading zero bit in the integer’s binary representation.
 Example 1:
 Input: 5
 Output: 2
 Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 Example 2:
 Input: 1
 Output: 0
 Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

 */

/**
 * @see https://leetcode.com/submissions/detail/101724190/
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    var binaryArray = num.toString(2).split('');
    var flippedBinary = binaryArray.map(function(bit) {
        return bit === '0' ? '1' : '0';
    });
    return parseInt(flippedBinary.join(''), 2);
};

var expect = require('../lib').expect;
expect(findComplement(5), 2);
expect(findComplement(1), 0);
