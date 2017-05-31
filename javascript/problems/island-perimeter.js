/**
 * @since 2017-05-11 10:13:15
 * @author vivaxy
 * @see https://leetcode.com/problems/island-perimeter/

 You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 Example:

 [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

 Answer: 16
 Explanation: The perimeter is the 16 yellow stripes in the image below:

 ![island](https://leetcode.com/static/images/problemset/island.png)

 */

/**
 * @see https://leetcode.com/submissions/detail/102590905/
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    var result = 0;
    for (var i = 0, iLength = grid.length; i < iLength; i++) {
        for (var j = 0, jLength = grid[i].length; j < jLength; j++) {
            var item = grid[i][j];
            if (item === 1) {
                if (j === 0 || grid[i][j - 1] !== 1) {
                    result++;
                }
                if (j === jLength - 1 || grid[i][j + 1] !== 1) {
                    result++;
                }
                if (i === 0 || grid[i - 1][j] !== 1) {
                    result++;
                }
                if (i === iLength - 1 || grid[i + 1][j] !== 1) {
                    result++;
                }
            }
        }
    }
    return result;
};

var test = require('ava');
test('island-perimeter', function(t) {
    t.is(islandPerimeter(
        [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
    ), 16);
});
