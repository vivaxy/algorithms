/**
 * @since 2017-06-09 21:26:44
 * @author vivaxy
 * @see https://leetcode.com/problems/first-bad-version/

 You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

 Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

 You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 */

/**
 * Definition for isBadVersion()
 *
 * @param {number} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @see https://leetcode.com/submissions/detail/105492090/
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * 二分法
     * @param {number} n Total versions
     * @return {number} The first bad version
     */
    return function(n) {
        var low = 1;
        var high = n;
        while (high - low > 1) {
            var version = parseInt((high - low) / 2) + low;
            if (isBadVersion(version)) {
                high = version;
            } else {
                low = version + 1;
            }
        }
        return isBadVersion(low) ? low : high;
    };
};

var test = require('ava');
test('main', function(t) {
    var isBadVersion = function(version) {
        return version >= 4;
    };
    t.is(solution(isBadVersion)(5), 4);

    var isBadVersion2 = function(version) {
        return version >= 1;
    };
    t.is(solution(isBadVersion2)(2), 1);

    var isBadVersion3 = function(version) {
        return version >= 2;
    };
    t.is(solution(isBadVersion3)(3), 2);
});
