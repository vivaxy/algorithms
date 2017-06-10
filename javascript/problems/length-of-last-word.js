/**
 * @since 2017-06-10 14:50:08
 * @author vivaxy
 * @see https://leetcode.com/problems/length-of-last-word/

 Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

 If the last word does not exist, return 0.

 Note: A word is defined as a character sequence consists of non-space characters only.

 For example,
 Given s = "Hello World",
 return 5.

 */

/**
 * @see https://leetcode.com/submissions/detail/105559400/
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    var words = s.split(' ');
    while (words.length > 1 && !words[words.length - 1]) {
        words.pop();
    }
    if (words.length === 0) {
        return 0;
    }
    if (words.length === 1) {
        return words[0].length;
    }
    return words[words.length - 1].length;
};

var test = require('ava');
test('main', function(t) {
    t.is(lengthOfLastWord('Hello World'), 5);
    t.is(lengthOfLastWord('a '), 1);
    t.is(lengthOfLastWord(''), 0);
    t.is(lengthOfLastWord('b   a    '), 1);
});
