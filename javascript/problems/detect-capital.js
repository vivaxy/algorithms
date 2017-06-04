/**
 * @since 2017-06-04 09:31:07
 * @author vivaxy
 * @see https://leetcode.com/problems/detect-capital/

 Given a word, you need to judge whether the usage of capitals in it is right or not.

 We define the usage of capitals in a word to be right when one of the following cases holds:

 All letters in this word are capitals, like "USA".
 All letters in this word are not capitals, like "leetcode".
 Only the first letter in this word is capital if it has more than one letter, like "Google".
 Otherwise, we define that this word doesn't use capitals in a right way.
 Example 1:
 Input: "USA"
 Output: True
 Example 2:
 Input: "FlaG"
 Output: False
 Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

 */

/**
 * @see https://leetcode.com/submissions/detail/104877607/
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if (word.length === 1) {
        return true;
    }

    var firstChar = word[0];
    var isFirstCharCapital = firstChar === firstChar.toUpperCase();

    var secondChar = word[1];
    var isSecondCharCapital = secondChar === secondChar.toUpperCase();

    // all/none/first
    var capitalMode = null;
    if (isFirstCharCapital && !isSecondCharCapital) {
        capitalMode = 'first';
    }
    if (isFirstCharCapital && isSecondCharCapital) {
        capitalMode = 'all';
    }
    if (!isFirstCharCapital && !isSecondCharCapital) {
        capitalMode = 'none';
    }
    if (capitalMode === null) {
        return false;
    }

    var cur = 2;
    while (cur < word.length) {
        var char = word[cur];
        if (capitalMode === 'first' && char.toUpperCase() === char) {
            return false;
        } else if (capitalMode === 'all' && char.toLowerCase() === char) {
            return false;
        } else if (capitalMode === 'none' && char.toUpperCase() === char) {
            return false;
        }
        cur++;
    }
    return true;
};

var test = require('ava');
test('main', function(t) {
    t.is(detectCapitalUse('USA'), true);
    t.is(detectCapitalUse('FlaG'), false);
});
