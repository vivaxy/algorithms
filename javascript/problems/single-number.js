/**
 * @since 2017-05-25 10:44:41
 * @author vivaxy
 * @see https://leetcode.com/problems/single-number/

 Given an array of integers, every element appears twice except for one. Find that single one.

 Note:
 Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

 */

/**
 * @see https://leetcode.com/submissions/detail/103949051/
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var savedNums = [];
    for (var i = 0; i < nums.length; i++) {
        var current = nums[i];
        var index = savedNums.indexOf(current);
        if (index === -1) {
            // not found
            savedNums.push(current);
        } else {
            savedNums.splice(index, 1);
        }
    }
    return savedNums[0];
};

var expect = require('../lib').expect;
expect(singleNumber([1]), 1);
expect(singleNumber([1, 2, 2]), 1);
expect(singleNumber([1, 2, 2, 1, 1]), 1);
