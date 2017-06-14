/**
 * @since 2017-06-14 19:48:31
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/single-element-in-a-sorted-array/

 Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

 Example 1:
 Input: [1,1,2,3,3,4,4,8,8]
 Output: 2
 Example 2:
 Input: [3,3,7,7,10,11,11]
 Output: 10

 */

/**
 * @see https://leetcode.com/submissions/detail/106025477/
 *
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    var result = 0;
    for (var i = 0, l = nums.length; i < l; i++) {
        if (result < 0) {
            return nums[i - 2];
        }
        if (result === 0) {
            result = result + nums[i];
        } else {
            result = result - nums[i];
        }
    }
    return result;
};

var test = require('ava');
test('main', function(t) {
    t.is(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]), 2);
    t.is(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]), 10);
});
