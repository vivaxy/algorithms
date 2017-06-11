/**
 * @since 2017-06-11 12:29:38
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/most-frequent-subtree-sum/

 Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

 Examples 1
 Input:

 5
 /  \
 2   -3
 return [2, -3, 4], since all the values happen only once, return all of them in any order.
 Examples 2
 Input:

 5
 /  \
 2   -5
 return [2], since 2 happens twice, however -5 only occur once.
 Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @see https://leetcode.com/submissions/detail/105656329/
 *
 * @param {TreeNode} root
 * @return {number[]}
 */
var findFrequentTreeSum = function(root) {
    var map = {};
    var maxCount = 0;
    var maxResult = [];
    var traverse = function(node) {
        if (!node) {
            return 0;
        }
        var subTreeSum = node.val + traverse(node.left) + traverse(node.right);
        if (map[subTreeSum] === undefined) {
            map[subTreeSum] = 0;
        }
        var count = map[subTreeSum] + 1;
        map[subTreeSum] = count;
        if (count > maxCount) {
            maxCount = count;
            maxResult = [subTreeSum];
        } else if (count === maxCount) {
            maxResult.push(subTreeSum);
        }
        return subTreeSum;
    };
    traverse(root);
    return maxResult;
};

var test = require('ava');
test('main', function(t) {
    var treeNode1 = {
        val: 5,
        left: {
            val: 2,
            left: null,
            right: null
        },
        right: {
            val: -3,
            left: null,
            right: null
        }
    };
    t.deepEqual(findFrequentTreeSum(treeNode1), [2, -3, 4]);

    var treeNode2 = {
        val: 5,
        left: {
            val: 2,
            left: null,
            right: null
        },
        right: {
            val: -5,
            left: null,
            right: null
        }
    };
    t.deepEqual(findFrequentTreeSum(treeNode2), [2]);
});
