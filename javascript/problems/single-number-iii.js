/**
 * @since 2017-06-16 09:43:39
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/single-number-iii/

 Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

 For example:

 Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

 Note:
 The order of the result is not important. So in the above example, [5, 3] is also correct.
 Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

 */

/**
 * @see https://leetcode.com/submissions/detail/106205998/
 *
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    var sortedNums = nums.sort(function(prev, next) {
        return prev - next;
    });
    var results = [];
    var sum = 0;
    for (var i = 0; i < sortedNums.length; i++) {
        if (sum === 0) {
            sum = sum + sortedNums[i];
        } else if (sum !== 0) {
            if (sum - sortedNums[i] === 0) {
                sum = 0;
            } else {
                results.push(sum);
                sum = sortedNums[i];
            }
        }
    }
    if (sum !== 0) {
        results.push(sum);
    }
    if (results.length < 2) {
        results.push(0);
    }
    return results;
};

var test = require('ava');
test('main', function(t) {
    t.deepEqual(singleNumber([-1, 0]), [-1, 0]);
    t.deepEqual(singleNumber([1, 2, 1, 3, 2, 5]), [3, 5]);
});
