/**
 * @since 2017-05-22 09:38:42
 * @author vivaxy
 * @see https://leetcode.com/problems/beautiful-arrangement/

 Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 ≤ i ≤ N) in this array:

 The number at the ith position is divisible by i.
 i is divisible by the number at the ith position.
 Now given N, how many beautiful arrangements can you construct?

 Example 1:
 Input: 2
 Output: 2
 Explanation:

 The first beautiful arrangement is [1, 2]:

 Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

 Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

 The second beautiful arrangement is [2, 1]:

 Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

 Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 Note:
 N is a positive integer and will not exceed 15.

 */

/**
 * @see https://leetcode.com/submissions/detail/103732980/
 *     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18  .  .  .
 *  1  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x
 *  2  x  x     x     x     x     x     x     x     x     x
 *  3  x     x        x        x        x        x        x
 *  4  x  x     x           x           x           x
 *  5  x           x              x              x
 *  6  x  x  x        x                 x                 x
 *  7  x                 x                    x
 *  8  x  x     x           x                       x
 *  9  x     x                 x                          x
 * 10  x  x        x              x
 * 11  x                             x
 * 12  x  x  x  x     x                 x
 * 13  x                                   x
 * 14  x  x              x                    x
 * 15  x     x     x                             x
 * 16  x  x     x           x                       x
 * 17  x                                               x
 * 18  x  x  x        x        x                          x
 *  .
 *  .
 *  .
 * @param {number} N
 * @return {number}
 */
var countArrangement = function(N) {
    var createArray = function(length) {
        var array = [];
        for (var i = 1; i < length + 1; i++) {
            array.push(i);
        }
        return array;
    };
    var count = 0;
    var arrange = function(array, position) {
        if (array.length === 0) {
            count++;
            return;
        }
        for (var i = 0; i < array.length; i++) {
            var nextArray = array.slice();
            var currentValue = nextArray.splice(i, 1)[0];
            if (position % currentValue === 0 || currentValue % position === 0) {
                arrange(nextArray, position + 1);
            }
        }
    };
    var array = createArray(N);
    arrange(array, 1);
    return count;
};

var test = require('ava');
test('beautiful-arrangement', function(t) {
    t.is(countArrangement(2), 2);
    t.is(countArrangement(3), 3);
    t.is(countArrangement(4), 8);
});
