/**
 * @since 2017-06-10 15:21:53
 * @author vivaxy
 * @see https://leetcode.com/problems/merge-sorted-array/

 Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

 Note:
 You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

 */

/**
 * @see https://leetcode.com/submissions/detail/105561848/
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    nums1.splice(m);
    loop: while (n--) {
        for (var i = 0; i < nums1.length; i++) {
            if (nums1[i] > nums2[n]) {
                nums1.splice(i, 0, nums2[n]);
                continue loop;
            }
        }
        nums1.push(nums2[n]);
    }
};

var test = require('ava');
test('main', function(t) {
    var array = [1, 4];
    merge(array, 2, [2, 3, 5], 3);
    t.deepEqual(array, [1, 2, 3, 4, 5]);

    var array2 = [0];
    merge(array2, 0, [1], 1);
    t.deepEqual(array2, [1]);
});
