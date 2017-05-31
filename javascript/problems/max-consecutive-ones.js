/**
 * @since 2017-05-24 10:27:55
 * @author vivaxy
 * @see https://leetcode.com/problems/max-consecutive-ones/

 Given a binary array, find the maximum number of consecutive 1s in this array.

 Example 1:
 Input: [1,1,0,1,1,1]
 Output: 3
 Explanation: The first two digits or the last three digits are consecutive 1s.
 The maximum number of consecutive 1s is 3.
 Note:

 The input array will only contain 0 and 1.
 The length of input array is a positive integer and will not exceed 10,000

 */

/**
 * @see https://leetcode.com/submissions/detail/103831503/
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var index = 0;
    var current = nums[index];
    var count = 0;
    var max = 0;
    while (current !== undefined) {
        if (current === 0) {
            count = 0;
        } else {
            count++;
        }
        if (count >= max) {
            max = count;
        }
        index++;
        current = nums[index];
    }
    return max;
};

var test = require('ava');
test('max-consecutive-ones', function(t) {
    t.is(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3);
});
