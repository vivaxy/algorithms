/**
 * @since 2017-06-09 21:43:22
 * @author vivaxy
 * @see https://leetcode.com/problems/valid-palindrome/

 Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 For example,
 "A man, a plan, a canal: Panama" is a palindrome.
 "race a car" is not a palindrome.

 Note:
 Have you consider that the string might be empty? This is a good question to ask during an interview.

 For the purpose of this problem, we define empty string as valid palindrome.

 */

/**
 * @see https://leetcode.com/submissions/detail/105493485/
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    var string = s.split('').reduce(function(str, cur) {
        if (!/^[a-zA-Z0-9]/.test(cur)) {
            return str;
        }
        return str + cur.toLowerCase();
    }, '');
    var index = 0;
    var mid = parseInt(string.length / 2);
    while (index < mid) {
        if (string[index] !== string[string.length - index - 1]) {
            return false;
        }
        index++;
    }
    return true;
};

var test = require('ava');
test('main', function(t) {
    t.is(isPalindrome('A man, a plan, a canal: Panama'), true);
    t.is(isPalindrome('race a car'), false);
    t.is(isPalindrome('a.'), true);
    t.is(isPalindrome('.a'), true);
    t.is(isPalindrome('ab@a'), true);
    t.is(isPalindrome('c#dc'), true);
    t.is(isPalindrome('0P'), false);
});
