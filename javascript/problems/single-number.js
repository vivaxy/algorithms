/**
 * @since 2017-05-25 10:44:41
 * @author vivaxy
 * @see https://leetcode.com/problems/single-number/

 Given an array of integers, every element appears twice except for one. Find that single one.

 Note:
 Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

 */

/**
 * @see
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var index = 0;
    var current = nums[index];
    while (current !== undefined) {

    }
};

var expect = require('../lib').expect;
expect(singleNumber([1]), 1);
expect(singleNumber([1, 2, 2]), 1);
expect(singleNumber([1, 2, 2, 1, 1]), 1);
