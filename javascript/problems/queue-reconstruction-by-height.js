/**
 * @since 2017-05-15 10:00:05
 * @author vivaxy
 * @see https://leetcode.com/problems/queue-reconstruction-by-height/

 Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

 Note:
 The number of people is less than 1,100.

 Example

 Input:
 [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

 Output:
 [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

 */

/**
 * 前一个值表示权重，需要下降到 0 开始，中间差 1
 * 后一个值表示顺序
 * 前一个值 + 后一个值 的结果排序
 * 相同的结果以后一个值排序
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    var peopleHeight = [];
    people.forEach(function(p) {
        var height = p[0];
        if (peopleHeight.indexOf(height) === -1) {
            peopleHeight.push(height);
        }
    });
    var sortedPeopleHeight = peopleHeight.sort(function(p, n) {
        return p - n;
    });
    return people.sort(function(prev, next) {
        var prevHeight = prev[0];
        var prevBeforeCount = prev[1];
        var prevWeight = sortedPeopleHeight.indexOf(prevHeight);
        var prevOrder = prevWeight + prevBeforeCount;
        var nextHeight = next[0];
        var nextBeforeCount = next[1];
        var nextWeight = sortedPeopleHeight.indexOf(nextHeight);
        var nextOrder = nextWeight + nextBeforeCount;
        var diff = prevOrder - nextOrder;
        console.log(prev, next, diff, prevBeforeCount - nextBeforeCount);
        if (diff === 0) {
            return prevBeforeCount - nextBeforeCount;
        }
        return diff;
    });
};

var expect = require('../lib').expect;
var isSameArray = require('../lib').isSameArray;
expect(isSameArray(reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]), [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]), true);
