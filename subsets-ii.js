/**
 * @since 2017-03-28 11:55:56
 * @author vivaxy
 * @see https://leetcode.com/problems/subsets-ii/

 Given a collection of integers that might contain duplicates, nums, return all possible subsets.

 Note: The solution set must not contain duplicate subsets.

 For example,
 If nums = [1,2,2], a solution is:

 ```
 [
 [2],
 [1],
 [1,2,2],
 [2,2],
 [1,2],
 []
 ]
 ```
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    var results = [];
    var isSameArray = function(a, b) {
        return JSON.stringify(a) === JSON.stringify(b);
    };
    var saveInResults = function(array) {
        for (var k = 0; k < results.length; k++) {
            if (isSameArray(results[k], array)) {
                return;
            }
        }
        results.push(array);
    };

    var pickOne = function(from, callback) {
        for (var i = from; i < nums.length; i++) {
            callback(nums[i], i);
        }
    };

    var pickTwo = function(from, callback) {
        pickOne(from, function(v1, index) {
            pickOne(index, function(v2) {
                callback([v1, v2]);
            });
        });
    };

    for (var l = 0; l < nums.length; l++) {
        // through length
        for (var i = 0; i < nums.length; i++) {
            // through from
        }
    }
    return results;
};

console.log(subsetsWithDup([1, 2, 2]));
console.log(JSON.stringify(subsetsWithDup([1, 2, 2])) === JSON.stringify([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]));
console.log(JSON.stringify(subsetsWithDup([1, 2, 3])) === JSON.stringify([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]));
