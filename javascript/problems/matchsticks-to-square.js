/**
 * @since 2017-04-19 10:27:39
 * @author vivaxy
 * @see https://leetcode.com/problems/matchsticks-to-square/

 Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

 Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

 Example 1:
 Input: [1,1,2,2,2]
 Output: true

 Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
 Example 2:
 Input: [3,3,3,3,4]
 Output: false

 Explanation: You cannot find a way to form a square with all the matchsticks.
 Note:
 The length sum of the given matchsticks is in the range of 0 to 10^9.
 The length of the given matchstick array will not exceed 15.

 */

/**
 * @see https://leetcode.com/submissions/detail/101226885/
 * @param {number[]} nums
 * @return {boolean}
 */
var makesquare = function(nums) {
    var numbersLength = nums.length;
    var sideCount = 4;
    if (numbersLength <= 0) {
        return false;
    }
    /**
     * from max to min
     * @type {Array.<number>}
     */
    var sortedNumbers = nums.sort(function(prev, next) {
        return prev < next;
    });
    var totalLength = sortedNumbers.reduce(function(acc, i) {
        return acc + i;
    }, 0);
    var sideLength = totalLength / sideCount;
    if (sideLength !== parseInt(sideLength, 10)) {
        return false;
    }
    var maxNumber = sortedNumbers[0];
    if (maxNumber > sideLength) {
        return false;
    }
    var dfs = function(numbers, numberCount, sides, index, size) {
        if (index === numberCount) {
            return sides.every(function(side) {
                return side === size;
            });
        }
        for (var i = 0; i < sideCount; i++) {
            if (sides[i] + numbers[index] > size) {
                continue;
            }
            sides[i] = sides[i] + numbers[index];
            if (dfs(numbers, numberCount, sides, index + 1, size)) {
                return true;
            }
            sides[i] = sides[i] - numbers[index];
        }
        return false;
    };
    var startingSides = [];
    for (var i = 0; i < sideCount; i++) {
        startingSides.push(0);
    }
    return dfs(sortedNumbers, numbersLength, startingSides, 0, sideLength);
};

var test = require('ava');
test('main', function(t) {
    t.is(makesquare([1, 1, 2, 2, 2]), true);
    t.is(makesquare([3, 3, 3, 3, 4]), false);
    t.is(makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]), true);
});
