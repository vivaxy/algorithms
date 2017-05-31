/**
 * @since 2017-05-01 09:31:05
 * @author vivaxy
 * @see https://leetcode.com/problems/reshape-the-matrix/

 In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

 You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

 The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

 If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 Example 1:
 Input:
 nums =
 [[1,2],
 [3,4]]
 r = 1, c = 4
 Output:
 [[1,2,3,4]]
 Explanation:
 The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
 Example 2:
 Input:
 nums =
 [[1,2],
 [3,4]]
 r = 2, c = 4
 Output:
 [[1,2],
 [3,4]]
 Explanation:
 There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
 Note:
 The height and width of the given matrix is in range [1, 100].
 The given r and c are all positive.

 */

/**
 * @see https://leetcode.com/submissions/detail/101635681/
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(nums, r, c) {
    var originalRow = nums.length;
    var originalCol = nums[0].length;
    if (originalCol * originalRow !== r * c) {
        return nums;
    }
    var output = [];
    for (var i = 0; i < r; i++) {
        var row = [];
        for (var j = 0; j < c; j++) {
            var current = i * c + j;
            var oR = parseInt(current / originalCol);
            var oC = current % originalCol;
            row.push(nums[oR][oC]);
        }
        output.push(row);
    }
    return output;
};

var test = require('ava');
test('reshape-the-matrix', function(t) {
    t.deepEqual(matrixReshape([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]]);
    t.deepEqual(matrixReshape([[1, 2], [3, 4]], 2, 4), [[1, 2], [3, 4]]);
});
