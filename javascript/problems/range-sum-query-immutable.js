/**
 * @since 2017-06-10 10:44:22
 * @author vivaxy
 * @see https://leetcode.com/problems/range-sum-query-immutable/

 Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

 Example:
 Given nums = [-2, 0, 3, -5, 2, -1]

 sumRange(0, 2) -> 1
 sumRange(2, 5) -> -1
 sumRange(0, 5) -> -3
 Note:
 You may assume that the array does not change.
 There are many calls to sumRange function.

 */

/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.array = nums;
    this.cache = {};
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    var cache = this.cache;
    var array = this.array;

    var key = JSON.stringify([i, j]);
    if (cache[key] !== undefined) {
        return cache[key];
    }
    var createJob = function(start, end) {
        var jobKey = JSON.stringify([start, end]);
        var value = cache[jobKey];
        if (value !== undefined) {
            return value;
        }
        if (start === end) {
            value = array[start];
            cache[jobKey] = value;
            return value;
        }
        if (start + 1 === end) {
            value = array[start] + array[end];
            cache[jobKey] = value;
            return value;
        }
        var mid = Math.floor((start + end) / 2);
        value = createJob(start, mid) + createJob(mid + 1, end);
        cache[jobKey] = value;
        return value;
    };
    return createJob(i, j);
};


/**
 * @see https://leetcode.com/submissions/detail/105545003/
 * @param {number[]} nums
 */
var NumArray2 = function(nums) {
    var sums = [];
    var sum = 0;
    for (var i = 0, l = nums.length; i < l; i++) {
        sum += nums[i];
        sums.push(sum);
    }
    this.sums = sums;
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray2.prototype.sumRange = function(i, j) {
    var sums = this.sums;
    if (i === 0) {
        return sums[j];
    }
    return sums[j] - sums[i - 1];
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = Object.create(NumArray).createNew(nums)
 * var param_1 = obj.sumRange(i,j)
 */

var test = require('ava');
test('main', function(t) {
    var obj = new NumArray([-2, 0, 3, -5, 2, -1]);
    t.is(obj.sumRange(0, 2), 1);
    t.is(obj.sumRange(2, 5), -1);
    t.is(obj.sumRange(0, 5), -3);

    var obj2 = new NumArray2([-2, 0, 3, -5, 2, -1]);
    t.is(obj2.sumRange(0, 2), 1);
    t.is(obj2.sumRange(2, 5), -1);
    t.is(obj2.sumRange(0, 5), -3);
});
