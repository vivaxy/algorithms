/**
 * @since 2017-06-10 17:00:57
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/number-of-segments-in-a-string/

 Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

 Please note that the string does not contain any non-printable characters.

 Example:

 Input: "Hello, my name is John"
 Output: 5

 */

/**
 * @see https://leetcode.com/submissions/detail/105566954/
 *
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    return s.split(' ').filter(function(section) {
        return !!section;
    }).length;
};

var test = require('ava');
test('main', function(t) {
    t.is(countSegments('Hello, my name is John'), 5);
    t.is(countSegments(''), 0);
    t.is(countSegments('       '), 0);
});
