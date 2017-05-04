/**
 * @since 2017-05-04 10:29:58
 * @author vivaxy
 * @see https://leetcode.com/problems/counting-bits/

 Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

 Example:
 For num = 5 you should return [0,1,1,2,1,2].

 Follow up:

 It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
 Space complexity should be O(n).
 Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

 */

/**
 * @see https://leetcode.com/submissions/detail/101927861/
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    var results = [];
    for (var i = 0; i <= num; i++) {
        var bits = i.toString(2);
        var bitArray = bits.split('');
        var count = bitArray.reduce(function(acc, bit) {
            return acc + (bit === '1' ? 1 : 0);
        }, 0);
        results.push(count);
    }
    return results;
};

var expect = require('./lib').expect;
var isSameArray = require('./lib').isSameArray;
expect(isSameArray(countBits(5), [0, 1, 1, 2, 1, 2]), true);
expect(isSameArray(countBits(2), [0, 1, 1]), true);
