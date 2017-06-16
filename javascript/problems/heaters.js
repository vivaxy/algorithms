/**
 * @since 2017-06-10 11:20:43
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/heaters/

 Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

 Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

 So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

 Note:
 Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
 Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
 As long as a house is in the heaters' warm radius range, it can be warmed.
 All the heaters follow your radius standard and the warm radius will the same.
 Example 1:
 Input: [1,2,3],[2]
 Output: 1
 Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 Example 2:
 Input: [1,2,3,4],[1,4]
 Output: 1
 Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

 */

/**
 * @param {number[]} houses
 * @param {number[]} heaters
 * @return {number}
 */
var findRadius = function(houses, heaters) {
    var sort = function(prev, next) {
        return prev - next;
    };
    heaters = heaters.sort(sort);
    var maxDistance = 0;
    for (var i = 0, houseLength = houses.length; i < houseLength; i++) {
        var house = houses[i];
        var minDistance = Infinity;
        for (var j = 0, heaterLength = heaters.length; j < heaterLength; j++) {
            var heater = heaters[j];
            var distance = Math.abs(heater - house);
            if (distance < minDistance) {
                minDistance = distance;
            }
        }
        if (minDistance > maxDistance) {
            maxDistance = minDistance;
        }
    }
    return maxDistance;
};

var test = require('ava');
test('main', function(t) {
    t.is(findRadius([1, 2, 3], [2]), 1);
    t.is(findRadius([1, 2, 3, 4], [1, 4]), 1);
    t.is(findRadius([1, 5], [2]), 3);
    t.is(findRadius([1, 2, 3, 5, 15], [2, 30]), 13);
    t.is(findRadius([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923], [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612]), 161834419);
});
