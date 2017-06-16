/**
 * @since 2017-06-09 22:06:52
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/count-primes/

 Count the number of prime numbers less than a non-negative number, n.

 */

/**
 * @see https://leetcode.com/submissions/detail/105494255/
 *
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    var index = 2;
    var results = 0;
    outer: while (index < n) {
        var i = 2;
        while (i <= Math.sqrt(index)) {
            if (index % i === 0) {
                index++;
                continue outer;
            }
            i++;
        }
        results++;
        index++;
    }
    return results;
};

var test = require('ava');
test('main', function(t) {
    t.is(countPrimes(5), 2);
    t.is(countPrimes(2), 0);
});
