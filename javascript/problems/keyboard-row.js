/**
 * @since 2017-05-06 11:28:04
 * @author vivaxy
 * @see https://leetcode.com/problems/keyboard-row/

 Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


 American keyboard


 Example 1:
 Input: ["Hello", "Alaska", "Dad", "Peace"]
 Output: ["Alaska", "Dad"]
 Note:
 You may use one character in the keyboard more than once.
 You may assume the input string will only contain letters of alphabet.

 */

/**
 * @see https://leetcode.com/submissions/detail/102112009/
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    var keyboardRows = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ];
    var findRowIndex = function(char) {
        for (var i = 0; i < keyboardRows.length; i++) {
            if (keyboardRows[i].indexOf(char.toLowerCase()) > -1) {
                return i;
            }
        }
    };
    var isWordsOnlyContainsLettersInOneRow = function(word) {
        var chars = word.split('');
        var thisRowIndex = findRowIndex(chars[0]);
        for (var i = 1; i < chars.length; i++) {
            if (findRowIndex(chars[i]) !== thisRowIndex) {
                return false;
            }
        }
        return true;
    };
    return words.filter(isWordsOnlyContainsLettersInOneRow);
};

var test = require('ava');
test('main', function(t) {
    t.deepEqual(findWords(['Hello', 'Alaska', 'Dad', 'Peace']), ['Alaska', 'Dad']);
});
