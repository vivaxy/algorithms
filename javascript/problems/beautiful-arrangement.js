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
    var matching = {};
    var count = 1;
    for (var i = 1; i <= N; i++) {
        // i => base
        var results = [];
        for (var j = 1; j <= N; j++) {
            // j => matching
            if (j < i) {
                if (matching[j].indexOf(i) !== -1) {
                    results.push(j);
                }
            } else if (j === i) {
                results.push(j);
            } else {
                if (j % i === 0) {
                    results.push(j);
                }
            }
        }
        count = count * results.length;
        matching[i] = results;
    }
    return count / 2;
};

var expect = require('../lib').expect;
expect(countArrangement(2), 2);
expect(countArrangement(3), 3);
