/**
 * @since 2017-06-10 10:08:27
 * @author vivaxy
 * @see https://leetcode.com/problems/k-diff-pairs-in-an-array/

 Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

 Example 1:
 Input: [3, 1, 4, 1, 5], k = 2
 Output: 2
 Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
 Although we have two 1s in the input, we should only return the number of unique pairs.
 Example 2:
 Input:[1, 2, 3, 4, 5], k = 1
 Output: 4
 Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
 Example 3:
 Input: [1, 3, 1, 5, 4], k = 0
 Output: 1
 Explanation: There is one 0-diff pair in the array, (1, 1).
 Note:
 The pairs (i, j) and (j, i) count as the same pair.
 The length of the array won't exceed 10,000.
 All the integers in the given input belong to the range: [-1e7, 1e7].

 */

/**
 * @see https://leetcode.com/submissions/detail/105542542/
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    if (k < 0) {
        return 0;
    }
    var startingPair = [];
    for (var i = 0, l = nums.length; i < l; i++) {
        var current = nums[i];
        var next = current + k;
        var nextIndex = nums.indexOf(next);
        if (nextIndex > -1 && nextIndex !== i) {
            if (startingPair.indexOf(current) === -1) {
                startingPair.push(current);
            }
        }
    }
    return startingPair.length;
};

var test = require('ava');
test('main', function(t) {
    t.is(findPairs([3, 1, 4, 1, 5], 2), 2);
    t.is(findPairs([1, 2, 3, 4, 5], 1), 4);
    t.is(findPairs([1, 3, 1, 5, 4], 0), 1);
    t.is(findPairs([1, 2, 3, 4, 5], -1), 0);
});
