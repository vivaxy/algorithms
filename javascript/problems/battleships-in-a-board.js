/**
 * @since 2017-05-03 10:52:50
 * @author vivaxy
 * @see https://leetcode.com/problems/battleships-in-a-board/

 Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

 You receive a valid board, made of only battleships or empty slots.
 Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
 At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
 Example:
 X..X
 ...X
 ...X
 In the above board there are 2 battleships.
 Invalid Example:
 ...X
 XXXX
 ...X
 This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
 Follow up:
 Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

 */

/**
 * @see https://leetcode.com/submissions/detail/101828331/
 * @param {String[][]} board
 * @return {number}
 */
var countBattleships = function(board) {
    var ships = 0;
    var XPositions = [];
    for (var i = 0; i < board.length; i++) {
        var row = board[i];
        for (var j = 0; j < row.length; j++) {
            if (row[j] === 'X') {
                XPositions.push({
                    x: i,
                    y: j
                });
                var isAdjacent = false;
                for (var k = 0; k < XPositions.length; k++) {
                    var currentXPosition = XPositions[k];
                    if (i === currentXPosition.x - 1 && j === currentXPosition.y) {
                        isAdjacent = true;
                    }
                    if (i === currentXPosition.x + 1 && j === currentXPosition.y) {
                        isAdjacent = true;
                    }
                    if (i === currentXPosition.x && j === currentXPosition.y - 1) {
                        isAdjacent = true;
                    }
                    if (i === currentXPosition.x && j === currentXPosition.y + 1) {
                        isAdjacent = true;
                    }
                }
                if (!isAdjacent) {
                    ships++;
                }
            }
        }
    }
    return ships;
};

/**
 * @see https://leetcode.com/submissions/detail/101830777/
 * @param {String[][]} board
 * @return {number}
 */
var countBattleships2 = function(board) {
    var ships = 0;
    for (var i = 0; i < board.length; i++) {
        for (var j = 0; j < board[i].length; j++) {
            if (board[i][j] === '.') continue;
            if (i !== 0 && board[i - 1][j] === 'X') continue;
            if (j !== 0 && board[i][j - 1] === 'X') continue;
            ships++;
        }
    }
    return ships;
};

var expect = require('../lib').expect;
expect(countBattleships(
    [
        ['X', '.', 'X'],
        ['.', '.', 'X'],
        ['.', '.', 'X']
    ]
), 2);
expect(countBattleships2(
    [
        ['X', '.', 'X'],
        ['.', '.', 'X'],
        ['.', '.', 'X']
    ]
), 2);
