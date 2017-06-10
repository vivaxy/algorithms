/**
 * @since 2017-06-10 09:54:32
 * @author vivaxy
 * @see https://leetcode.com/problems/implement-strstr/

 Implement strStr().

 Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 */

/**
 * @see https://leetcode.com/submissions/detail/105539724/
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};

var test = require('ava');
test('main', function(t) {
    t.is(strStr('', ''), 0);
});
