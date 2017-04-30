/**
 * @since 2017-04-30 10:07:40
 * @author vivaxy
 * @see https://leetcode.com/problems/reverse-words-in-a-string-iii/

 Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 Example 1:
 Input: "Let's take LeetCode contest"
 Output: "s'teL ekat edoCteeL tsetnoc"
 Note: In the string, each word is separated by single space and there will not be any extra space in the string.

 */

/**
 * @see https://leetcode.com/submissions/detail/101549082/
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.split(' ').map(function(word) {
        return word.split('').reverse().join('');
    }).join(' ');
};

console.log(reverseWords('Let\'s take LeetCode contest') === 's\'teL ekat edoCteeL tsetnoc');
