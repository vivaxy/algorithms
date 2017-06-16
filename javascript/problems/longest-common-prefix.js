/**
 * @since 2017-06-10 14:36:46
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/longest-common-prefix/

 Write a function to find the longest common prefix string amongst an array of strings.

 */

/**
 * @see https://leetcode.com/submissions/detail/105558891/
 *
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return '';
    }
    if (strs.length === 1) {
        return strs[0];
    }
    var commentPrefix = '';
    var minLength = Math.min.apply(Math, strs.map(function(str) {
        return str.length;
    }));
    var index = -1;
    while (index++ < minLength - 1) {
        for (var i = 0; i < strs.length - 1; i++) {
            if (strs[i][index] !== strs[i + 1][index]) {
                return commentPrefix;
            }
        }
        commentPrefix += strs[0][index];
    }
    return commentPrefix;
};

var test = require('ava');
test('main', function(t) {
    t.is(longestCommonPrefix(['abc', 'abcd']), 'abc');
    t.is(longestCommonPrefix(['abce', 'abcd']), 'abc');
    t.is(longestCommonPrefix([]), '');
    t.is(longestCommonPrefix(['']), '');
    t.is(longestCommonPrefix(['', '']), '');
});
