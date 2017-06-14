/**
 * @since 2017-06-14 10:02:39
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/find-the-difference/

 Given two strings s and t which consist of only lowercase letters.

 String t is generated by random shuffling string s and then add one more letter at a random position.

 Find the letter that was added in t.

 Example:

 Input:
 s = "abcd"
 t = "abcde"

 Output:
 e

 Explanation:
 'e' is the letter that was added.

 */

/**
 * @see https://leetcode.com/submissions/detail/105974730/
 *
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var findTheDifference = function(s, t) {
    var sList = s.split('');
    var tList = t.split('');
    for (var i = 0, l = sList.length; i < l; i++) {
        var char = sList[i];
        var tIndex = tList.indexOf(char);
        tList.splice(tIndex, 1);
    }
    return tList[0];
};

var test = require('ava');
test('main', function(t) {
    t.is(findTheDifference('abcd', 'abcde'), 'e');
    t.is(findTheDifference('a', 'aa'), 'a');
});
