/**
 * @since 2017-06-10 17:18:32
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/search-insert-position/

 Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 You may assume no duplicates in the array.

 Here are few examples.
 [1,3,5,6], 5 → 2
 [1,3,5,6], 2 → 1
 [1,3,5,6], 7 → 4
 [1,3,5,6], 0 → 0

 */

/**
 * @see https://leetcode.com/submissions/detail/105568722/
 *
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var find = function(begin, end) {
        if (begin + 1 === end || begin === end) {
            if (target > nums[end]) {
                return end + 1;
            } else if (target <= nums[begin]) {
                return begin;
            }
            return end;
        }
        var mid = Math.floor((begin + end) / 2);
        if (nums[mid] >= target) {
            return find(begin, mid);
        }
        return find(mid + 1, end);
    };
    return find(0, nums.length - 1);
};

var test = require('ava');
test('main', function(t) {
    t.is(searchInsert([1, 3, 5, 6], 5), 2);
    t.is(searchInsert([1, 3, 5, 6], 2), 1);
    t.is(searchInsert([1, 3, 5, 6], 7), 4);
    t.is(searchInsert([1, 3, 5, 6], 0), 0);
    t.is(searchInsert([1], 2), 1);
});
