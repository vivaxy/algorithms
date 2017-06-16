/**
 * @since 2017-06-09 20:04:40
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/rotate-array/

 Rotate an array of n elements to the right by k steps.

 For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

 Note:
 Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

 [show hint]

 Related problem: Reverse Words in a String II

 Credits:
 Special thanks to @Freezen for adding this problem and creating all test cases.

 */

/**
 * @see https://leetcode.com/submissions/detail/105487953/
 *
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    while (k) {
        nums.unshift(nums.pop());
        k--;
    }
};

/**
 * @see https://leetcode.com/submissions/detail/105488060/
 *
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate2 = function(nums, k) {
    nums.splice.apply(nums, [0, 0].concat(nums.splice(nums.length - k, k)));
};

var test = require('ava');
test('main', function(t) {
    var nums = [1, 2, 3, 4, 5, 6, 7];
    rotate(nums, 3);
    t.deepEqual(nums, [5, 6, 7, 1, 2, 3, 4]);

    var nums2 = [1, 2, 3, 4, 5, 6, 7];
    rotate2(nums2, 3);
    t.deepEqual(nums2, [5, 6, 7, 1, 2, 3, 4]);

});
