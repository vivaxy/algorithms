/**
 * @since 2017-06-09 11:09:15
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/maximum-depth-of-binary-tree/

 Given a binary tree, find its maximum depth.

 The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 * @typedef {Object} TreeNode
 * @property {number} val
 * @property {?TreeNode} left
 * @property {?TreeNode} right
 */
/**
 * @see https://leetcode.com/submissions/detail/105447489/
 *
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    var traverse = function(node, depth) {
        if (!node) {
            return depth;
        }
        return Math.max(traverse(node.left, depth + 1), traverse(node.right, depth + 1));
    };
    return traverse(root, 0);
};

var test = require('ava');
test('main', function(t) {
    var tree = {
        val: 1
    };
    t.is(maxDepth(tree), 1);
});
