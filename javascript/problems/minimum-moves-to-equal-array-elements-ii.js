/**
 * @since 2017-06-15 19:54:36
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

 Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

 You may assume the array's length is at most 10,000.

 Example:

 Input:
 [1,2,3]

 Output:
 2

 Explanation:
 Only two moves are needed (remember each move increments or decrements one element):

 [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

 */

/**
 * @see https://leetcode.com/submissions/detail/106142122/
 *
 * @param {number[]} nums
 * @return {number}
 */
var minMoves2 = function(nums) {
    var sortedNums = nums.sort(function(prev, next) {
        return prev - next;
    });
    var avg = sortedNums[Math.floor(sortedNums.length / 2)];
    var moves = 0;
    for (var j = 0; j < nums.length; j++) {
        moves = moves + Math.abs(nums[j] - avg);
    }
    return moves;
};

var test = require('ava');
test('main', function(t) {
    t.is(minMoves2([1, 2, 3]), 2);
    t.is(minMoves2([1, 0, 0, 8, 6]), 14);
});
