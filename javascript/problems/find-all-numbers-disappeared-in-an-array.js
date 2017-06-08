/**
 * @since 2017-06-08 10:02:30
 * @author vivaxy
 * @see https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

 Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

 Find all the elements of [1, n] inclusive that do not appear in this array.

 Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

 Example:

 Input:
 [4,3,2,7,8,2,3,1]

 Output:
 [5,6]

 */

/**
 * @see https://leetcode.com/submissions/detail/105328465/
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    var array = [];
    nums.forEach(function(num) {
        array[num] = true;
    });
    var results = [];
    for (var i = 1; i <= nums.length; i++) {
        if (!array[i]) {
            results.push(i);
        }
    }
    return results;
};

var test = require('ava');
test('main', function(t) {
    t.deepEqual(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6]);
});
