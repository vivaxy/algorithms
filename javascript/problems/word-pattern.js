/**
 * @since 2017-06-10 16:13:39
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/word-pattern/

 Given a pattern and a string str, find if str follows the same pattern.

 Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

 Examples:
 pattern = "abba", str = "dog cat cat dog" should return true.
 pattern = "abba", str = "dog cat cat fish" should return false.
 pattern = "aaaa", str = "dog cat cat dog" should return false.
 pattern = "abba", str = "dog dog dog dog" should return false.
 Notes:
 You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

 */

/**
 * @see https://leetcode.com/submissions/detail/105565285/
 *
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPattern = function(pattern, str) {
    var strSections = str.split(' ');
    var patterns = pattern.split('');
    if (patterns.length !== strSections.length) {
        return false;
    }
    var map = {};
    var patternInMap = [];
    for (var i = 0; i < patterns.length; i++) {
        if (map[patterns[i]]) {
            if (map[patterns[i]] !== strSections[i]) {
                return false;
            }
        } else {
            if (patternInMap.indexOf(strSections[i]) === -1) {
                patternInMap.push(strSections[i]);
                map[patterns[i]] = strSections[i];
            } else {
                return false;
            }
        }
    }
    return true;
};

var test = require('ava');
test('main', function(t) {
    t.is(wordPattern('abba', 'dog cat cat dog'), true);
    t.is(wordPattern('abba', 'dog cat cat fish'), false);
    t.is(wordPattern('aaaa', 'dog cat cat dog'), false);
    t.is(wordPattern('abba', 'dog dog dog dog'), false);
});
