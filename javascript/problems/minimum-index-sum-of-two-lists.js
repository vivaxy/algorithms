/**
 * @since 2017-05-29 10:47:18
 * @author vivaxy
 * @see https://leetcode.com/problems/minimum-index-sum-of-two-lists/
 Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

 You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

 Example 1:
 Input:
 ["Shogun", "Tapioca Express", "Burger King", "KFC"]
 ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
 Output: ["Shogun"]
 Explanation: The only restaurant they both like is "Shogun".
 Example 2:
 Input:
 ["Shogun", "Tapioca Express", "Burger King", "KFC"]
 ["KFC", "Shogun", "Burger King"]
 Output: ["Shogun"]
 Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
 Note:
 The length of both lists will be in the range of [1, 1000].
 The length of strings in both lists will be in the range of [1, 30].
 The index is starting from 0 to the list length minus 1.
 No duplicates in both lists.

 */

/**
 * @see https://leetcode.com/submissions/detail/104312353/
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    var results = [];
    var min = Infinity;
    for (var j = 0; j < list2.length; j++) {
        var item = list2[j];
        var i = list1.indexOf(item);
        if (i !== -1) {
            var sum = i + j;
            if (sum < min) {
                results = [item];
                min = sum;
            } else if (sum === min) {
                results.push(item);
            }
        }
    }
    return results;
};

var test = require('ava');
test('minimum-index-sum-of-two-lists', function(t) {
    t.deepEqual(findRestaurant(
        ['Shogun', 'Tapioca Express', 'Burger King', 'KFC'],
        ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']
    ), ['Shogun']);
    t.deepEqual(findRestaurant(
        ['Shogun', 'Tapioca Express', 'Burger King', 'KFC'],
        ['KFC', 'Shogun', 'Burger King']
    ), ['Shogun']);
    t.deepEqual(findRestaurant(
        ['Shogun', 'Tapioca Express', 'Burger King', 'KFC'],
        ['KFC', 'Burger King', 'Tapioca Express', 'Shogun']
    ), ['KFC', 'Burger King', 'Tapioca Express', 'Shogun']);
});
