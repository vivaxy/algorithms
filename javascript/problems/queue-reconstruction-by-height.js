/**
 * @since 2017-05-15 10:00:05
 * @author vivaxy
 *
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
 * @see https://leetcode.com/submissions/detail/103145734/
 *
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    var sortedPeople = people.sort(function(prev, next) {
        var prevHeight = prev[0];
        var nextHeight = next[0];
        if (prevHeight === nextHeight) {
            return prev[1] - next[1];
        }
        return prevHeight - nextHeight;
    });
    var maxCursor = sortedPeople.length - 1;
    for (var cursor = maxCursor; cursor >= 0; cursor--) {
        var thisPerson = sortedPeople[cursor];
        var thisHeight = thisPerson[0];
        var thisOrder = thisPerson[1];
        var nowOrder = 0;
        for (var i = 0; i < cursor; i++) {
            if (sortedPeople[i][0] >= thisHeight) {
                nowOrder++;
            }
        }
        var orderDiff = thisOrder - nowOrder;
        if (orderDiff !== 0) {
            var targetPosition = cursor + orderDiff;
            sortedPeople.splice(cursor, 1);
            sortedPeople.splice(targetPosition, 0, thisPerson);
        }
    }
    return sortedPeople;
};

/**
 * 1. 正序，其中高度相同的按照 person[1] 倒序
 * 2. 从最后一个开始把人放进新的队列中，放到第 person[1] 位
 *
 * @see https://leetcode.com/submissions/detail/103266407/
 *
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue2 = function(people) {
    var sortedPeople = people.sort(function(prev, next) {
        var prevHeight = prev[0];
        var nextHeight = next[0];
        if (prevHeight === nextHeight) {
            return next[1] - prev[1];
        }
        return prevHeight - nextHeight;
    });
    var result = [];
    while (sortedPeople.length) {
        var thisPerson = sortedPeople.pop();
        result.splice(thisPerson[1], 0, thisPerson);
    }
    return result;
};

var test = require('ava');
test('main', function(t) {
    t.deepEqual(
        reconstructQueue(
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        ),
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    );
    t.deepEqual(
        reconstructQueue2(
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        ),
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    );
});
