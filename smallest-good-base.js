/**
 * @since 2017-04-02 09:52:31
 * @author vivaxy
 * @see https://leetcode.com/problems/smallest-good-base/

 For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

 Now given a string representing n, you should return the smallest good base of n in string format.

 Example 1:
 Input: "13"
 Output: "3"
 Explanation: 13 base 3 is 111.
 Example 2:
 Input: "4681"
 Output: "8"
 Explanation: 4681 base 8 is 11111.
 Example 3:
 Input: "1000000000000000000"
 Output: "999999999999999999"
 Explanation: 1000000000000000000 base 999999999999999999 is 11.
 Note:
 The range of n is [3, 10^18].
 The string representing n is always valid and will not have leading zeros.

 */

/**
 * 寻找进制
 * @see
 * @param {string} n
 * @return {string}
 */
var smallestGoodBase = function(n) {
    var calculate = function(input, k) {
        var nextInput = (input - 1) / k;
        if (nextInput === 1) {
            return true;
        } else if (nextInput > 1) {
            return calculate(nextInput, k);
        } else {
            return false;
        }
    };
    var input = Number(n);
    for (var base = 2; base < Infinity; base++) {
        if (calculate(input, base)) {
            return String(base);
        }
    }
};

console.log(smallestGoodBase('13') === '3');
console.log(smallestGoodBase('4681') === '8');
console.log(smallestGoodBase('1000000000000000000') === '999999999999999999');
