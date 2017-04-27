/**
 * @since 2017-04-27 09:53:29
 * @author vivaxy
 * @see https://leetcode.com/problems/array-partition-i/

 Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

 Example 1:
 Input: [1,4,3,2]

 Output: 4
 Explanation: n is 2, and the maximum sum of pairs is 4.
 Note:
 n is a positive integer, which is in the range of [1, 10000].
 All the integers in the array will be in the range of [-10000, 10000].

 */

/**
 * @see https://leetcode.com/submissions/detail/101303358/
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    var sortedNumbers = nums.sort(function(prev, next) {
        return prev - next;
    });
    return sortedNumbers.reduce(function(acc, val, index) {
        if (index % 2 === 0) {
            return acc + val;
        }
        return acc;
    }, 0);
};

console.log(arrayPairSum([1, 4, 3, 2]) === 4);
console.log(arrayPairSum([11, 41, -9046, 2047, 1118, 8477, 8446, 279, 4925, 7380, -1719, 3855]) === 6662);
