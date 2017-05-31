/**
 * @since 2017-05-30 10:29:27
 * @author vivaxy
 * @see https://leetcode.com/problems/find-largest-value-in-each-tree-row/
 You need to find the largest value in each row of a binary tree.

 Example:
 Input:

 1
 / \
 3   2
 / \   \
 5   3   9

 Output: [1, 3, 9]

 */

/**
 * @see https://leetcode.com/submissions/detail/104394005/
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @typedef {Object} TreeNode
 * @property {?TreeNode} left
 * @property {?TreeNode} right
 * @property {number} val
 *
 * @param {TreeNode} root
 * @return {number[]}
 */
var largestValues = function(root) {
    var results = [];
    var getNextNodes = function(nodes) {
        return nodes.reduce(function(acc, cur) {
            var left = cur.left;
            var right = cur.right;
            if (left && right) {
                return acc.concat(left, right);
            } else if (left) {
                return acc.concat(left);
            } else if (right) {
                return acc.concat(right);
            }
            return acc;
        }, []);
    };
    var getCurrentDepthMax = function(nodes) {
        return Math.max.apply(Math, nodes.map(function(node) {
            return node.val;
        }));
    };
    var traverse = function(currentNodes) {
        results.push(getCurrentDepthMax(currentNodes));
        var nextNodes = getNextNodes(currentNodes);
        if (nextNodes.length) {
            traverse(nextNodes);
        }
    };
    if (root) {
        traverse([root]);
    }
    return results;
};

var test = require('ava');
test('find-largest-value-in-each-tree-row', function(t) {
    var treeNode = {
        val: 1,
        left: {
            val: 3,
            left: {
                val: 5,
                left: null,
                right: null
            },
            right: {
                val: 3,
                left: null,
                right: null
            }
        },
        right: {
            val: 2,
            left: null,
            right: {
                val: 9,
                left: null,
                right: null
            }
        }
    };
    t.deepEqual(largestValues(treeNode), [1, 3, 9]);
    t.deepEqual(largestValues(null), []);
});
