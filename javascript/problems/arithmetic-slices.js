/**
 * @since 2017-05-19 10:04:51
 * @author vivaxy
 * @see https://leetcode.com/problems/arithmetic-slices/

 A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

 For example, these are arithmetic sequence:

 1, 3, 5, 7, 9
 7, 7, 7, 7
 3, -1, -5, -9
 The following sequence is not arithmetic.

 1, 1, 2, 5, 7

 A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

 A slice (P, Q) of array A is called arithmetic if the sequence:
 A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

 The function should return the number of arithmetic slices in the array A.


 Example:

 A = [1, 2, 3, 4]

 return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

 */

/**
 * @see https://leetcode.com/submissions/detail/103465675/
 * 1. [1, 2, 3, 4] diff => [1, 1, 1]
 * 2. find sibling same items, get length
 * 3. (n - 1) * (n - 2) / 2, where n is the array length, as previous step's result + 1
 * @param {number[]} A
 * @return {number}
 */
var numberOfArithmeticSlices = function(A) {
    var diffArray = [];
    for (var i = 0; i < A.length - 1; i++) {
        diffArray.push(A[i + 1] - A[i]);
    }
    var resultsArray = [];
    var current = 0;
    for (var j = 0; j < diffArray.length - 1; j++) {
        if (diffArray[j] === diffArray[j + 1]) {
            current++;
        } else {
            resultsArray.push(current + 2);
            current = 0;
        }
    }
    if (current > 0) {
        resultsArray.push(current + 2);
    }
    return resultsArray.reduce(function(acc, cur) {
        return (cur - 1) * (cur - 2) / 2 + acc;
    }, 0);
};

var expect = require('../lib').expect;
expect(numberOfArithmeticSlices([1, 2, 3, 4]), 3);
