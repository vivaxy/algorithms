/**
 * @since 2017-03-31 10:48:50
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/excel-sheet-column-title/

 Given a positive integer, return its corresponding column title as appear in an Excel sheet.

 For example:

 1 -> A
 2 -> B
 3 -> C
 ...
 26 -> Z
 27 -> AA
 28 -> AB

 */

/**
 * @see https://leetcode.com/submissions/detail/98612789/
 *
 * @param {number} n
 * @return {string}
 */
var convertToTitle = function(n) {
    var startingCharCode = 65;
    var system = 26;
    var results = '';
    var getDigital = function(value) {
        var remaining = value % system;
        var nextValue = parseInt(value / system, 10);
        results = String.fromCharCode(startingCharCode + remaining) + results;
        if (nextValue > 0) {
            getDigital(nextValue - 1);
        }
    };
    getDigital(n - 1);
    return results;
};

var test = require('ava');
test('main', function(t) {
    t.is(convertToTitle(1), 'A');
    t.is(convertToTitle(26), 'Z');
    t.is(convertToTitle(28), 'AB');
});
