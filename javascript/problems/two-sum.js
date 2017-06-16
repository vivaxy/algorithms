/**
 * @since 2017-06-10 16:33:54
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/two-sum/

 Given an array of integers, return indices of the two numbers such that they add up to a specific target.

 You may assume that each input would have exactly one solution, and you may not use the same element twice.

 Example:
 Given nums = [2, 7, 11, 15], target = 9,

 Because nums[0] + nums[1] = 2 + 7 = 9,
 return [0, 1].

 */

/**
 * @see https://leetcode.com/submissions/detail/105565540/
 *
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (var i = 0, l = nums.length; i < l; i++) {
        var a = nums[i];
        for (var j = i + 1; j < l; j++) {
            var b = nums[j];
            if (a + b === target) {
                return [i, j];
            }
        }
    }
};

var test = require('ava');
test('main', function(t) {
    t.deepEqual(twoSum([2, 7, 11, 15], 9), [0, 1]);
});
