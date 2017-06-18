/**
 * @since 2017-06-18 08:29:54
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/sort-characters-by-frequency/

 Given a string, sort it in decreasing order based on the frequency of characters.

 Example 1:

 Input:
 "tree"

 Output:
 "eert"

 Explanation:
 'e' appears twice while 'r' and 't' both appear once.
 So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
 Example 2:

 Input:
 "cccaaa"

 Output:
 "cccaaa"

 Explanation:
 Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
 Note that "cacaca" is incorrect, as the same characters must be together.
 Example 3:

 Input:
 "Aabb"

 Output:
 "bbAa"

 Explanation:
 "bbaA" is also a valid answer, but "Aabb" is incorrect.
 Note that 'A' and 'a' are treated as two different characters.

 */

/**
 * @see https://leetcode.com/submissions/detail/106393003/
 *
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    var maps = s.split('').reduce(function(map, char) {
        if (map[char] === undefined) {
            map[char] = 0;
        }
        map[char]++;
        return map;
    }, {});
    return Object.keys(maps).sort(function(prev, next) {
        return maps[next] - maps[prev];
    }).reduce(function(acc, key) {
        var count = maps[key];
        for (var i = 0; i < count; i++) {
            acc = acc + key;
        }
        return acc;
    }, '');
};

var test = require('ava');
test('main', function(t) {
    t.is(frequencySort('tree'), 'eetr');
    t.is(frequencySort('cccaaa'), 'cccaaa');
    t.is(frequencySort('Aabb'), 'bbAa');
});
