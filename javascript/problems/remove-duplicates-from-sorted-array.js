/**
 * @since 2017-06-10 16:41:06
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/remove-duplicates-from-sorted-array/

 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

 Do not allocate extra space for another array, you must do this in place with constant memory.

 For example,
 Given input array nums = [1,1,2],

 Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

 */

/**
 * @see https://leetcode.com/submissions/detail/105566407/
 *
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    for (var i = 1, l = nums.length; i < l; i++) {
        if (nums[i] === nums[i - 1]) {
            nums.splice(i, 1);
            i--;
            l = nums.length;
        }
    }
    return nums.length;
};

var test = require('ava');
test('main', function(t) {
    var array1 = [1, 1, 2];
    t.deepEqual(removeDuplicates(array1), 2);
    t.deepEqual(array1, [1, 2]);

    var array2 = [1, 2];
    t.deepEqual(removeDuplicates(array2), 2);
    t.deepEqual(array2, [1, 2]);

    var array3 = [1, 1, 1];
    t.deepEqual(removeDuplicates(array3), 1);
    t.deepEqual(array3, [1]);
});
