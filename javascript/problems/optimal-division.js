/**
 * @since 2017-05-13 09:48:05
 * @author vivaxy
 * @see https://leetcode.com/problems/optimal-division/

 Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

 However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

 Example:
 Input: [1000,100,10,2]
 Output: "1000/(100/10/2)"
 Explanation:
 1000/(100/10/2) = 1000/((100/10)/2) = 200
 However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
 since they don't influence the operation priority. So you should return "1000/(100/10/2)".

 Other cases:
 1000/(100/10)/2 = 50
 1000/(100/(10/2)) = 50
 1000/100/10/2 = 0.5
 1000/100/(10/2) = 2
 Note:

 The length of the input array is [1, 10].
 Elements in the given array will be in range [2, 1000].
 There is only one optimal division for each test case.

 */

/**
 * nums[0] / nums[1] * nums[2] * ...
 * nums[0] / (nums[1] / nums[2] / ...)
 * @see https://leetcode.com/submissions/detail/102770045/
 * @param {number[]} nums
 * @return {string}
 */
var optimalDivision = function(nums) {
    var beginning = String(nums.shift());
    if (!nums.length) {
        return beginning;
    }
    if (nums.length === 1) {
        return beginning + '/' + nums[0];
    }
    return beginning + '/(' + nums.join('/') + ')';
};

var expect = require('../lib').expect;
expect(optimalDivision([1000, 100, 10, 2]), '1000/(100/10/2)');
expect(optimalDivision([1000]), '1000');
expect(optimalDivision([1000, 10]), '1000/10');
