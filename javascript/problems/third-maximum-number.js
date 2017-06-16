/**
 * @since 2017-06-10 09:37:23
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/third-maximum-number/

 Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

 Example 1:
 Input: [3, 2, 1]

 Output: 1

 Explanation: The third maximum is 1.
 Example 2:
 Input: [1, 2]

 Output: 2

 Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
 Example 3:
 Input: [2, 2, 3, 1]

 Output: 1

 Explanation: Note that the third maximum here means the third maximum distinct number.
 Both numbers with value 2 are both considered as second maximum.

 */

/**
 * @see https://leetcode.com/submissions/detail/105539524/
 *
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    var max1 = -Infinity;
    var max2 = -Infinity;
    var max3 = -Infinity;
    for (var i = 0, l = nums.length; i < l; i++) {
        var current = nums[i];
        if (max1 < current) {
            max3 = max2;
            max2 = max1;
            max1 = current;
        } else if (max2 < current && max1 !== current) {
            max3 = max2;
            max2 = current;
        } else if (max3 < current && max2 !== current && max1 !== current) {
            max3 = current;
        }
    }
    if (max3 === -Infinity) {
        return max1;
    }
    return max3;
};

var test = require('ava');
test('main', function(t) {
    t.is(thirdMax([3, 2, 1]), 1);
    t.is(thirdMax([1, 2]), 2);
    t.is(thirdMax([2, 2, 3, 1]), 1);
    t.is(thirdMax([1, 2, -2147483648]), -2147483648);
});
