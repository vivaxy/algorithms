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
 * @see https://leetcode.com/submissions/detail/98492145/
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums = nums.sort(function(a, b) {
        return a > b;
    });
    var results = [[]];
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

    var pick = function(subArray, n, array) {
        // get n from subArray
        // get one from subArray, then get n-1 from next subArray
        for (var i = 0; i < subArray.length - (n - 1); i++) {
            var current = subArray[i];
            var nextSubArray = subArray.slice(i + 1);
            var resultArray = array.slice();
            resultArray.push(current);
            if (n - 1 > 0) {
                pick(nextSubArray, n - 1, resultArray);
            } else {
                // do things
                saveInResults(resultArray);
            }
        }
    };

    for (var i = 0; i < nums.length; i++) {
        pick(nums, i + 1, []);
    }

    return results;
};

var test = require('ava');
test('main', function(t) {
    t.deepEqual(subsetsWithDup([1, 2, 2]), [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]);
    t.deepEqual(subsetsWithDup([1, 2, 3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]);
});
