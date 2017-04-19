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
 * @param {number[]} nums
 * @return {boolean}
 */
var makesquare = function(nums) {
    var numbersLength = nums.length;
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
    var sideLength = totalLength / 4;
    if (sideLength !== parseInt(sideLength, 10)) {
        return false;
    }
    var maxNumber = sortedNumbers[0];
    if (maxNumber > sideLength) {
        return false;
    }
    var loopThroughArray = function(array, groupSize, groupCount) {
        var length = array.length;
        if (groupCount <= 0) {
            return length === 0;
        }
        var i = 0;
        var acceptedIndex = [];
        var remainingSize = groupSize;
        for (; i < length; i++) {
            if (remainingSize === 0) {
                break;
            }
            var current = array[i];
            if (current <= remainingSize) {
                acceptedIndex.push(i);
                remainingSize = remainingSize - current;
            } else {
                return false;
            }
        }
        if (remainingSize === 0) {
            var nextArray = array;
            acceptedIndex.reverse().forEach(function(index) {
                nextArray = nextArray.slice();
                nextArray.splice(index, 1);
            });
            return loopThroughArray(nextArray, groupSize, groupCount - 1);
        } else {
            return false;
        }
    };
    return loopThroughArray(sortedNumbers, sideLength, 4);
};

// console.log(makesquare([1, 1, 2, 2, 2]) === true);
// console.log(makesquare([3, 3, 3, 3, 4]) === false);
console.log(makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) === true);
