/**
 * @since 2017-05-12 10:10:30
 * @author vivaxy
 * @see https://leetcode.com/problems/find-bottom-left-tree-value/

 Given a binary tree, find the leftmost value in the last row of the tree.

 Example 1:
 Input:

 2
 / \
 1   3

 Output:
 1
 Example 2:
 Input:

 1
 / \
 2   3
 /   / \
 4   5   6
 /
 7

 Output:
 7
 Note: You may assume the tree (i.e., the given root node) is not NULL.

 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 * @typedef {Object} TreeNode
 * @property {TreeNode} [left]
 * @property {TreeNode} [right]
 * @property {Number} val
 */
/**
 * @see https://leetcode.com/submissions/detail/102690158/
 * @param {TreeNode} root
 * @return {number}
 */
var findBottomLeftValue = function(root) {
    var maxDepth = 0;
    var parseTreeNode = function(node, currentDepth) {
        maxDepth = currentDepth;
        if (node.left) {
            var leftResult = parseTreeNode(node.left, currentDepth + 1);
            if (node.right) {
                var rightResult = parseTreeNode(node.right, currentDepth + 1);
                if (rightResult.depth > leftResult.depth) {
                    return rightResult;
                }
            }
            return leftResult;
        }
        // without left node
        if (node.right) {
            return parseTreeNode(node.right, currentDepth + 1);
        }
        // without left and right node
        return {
            val: node.val,
            depth: currentDepth
        };
    };
    return parseTreeNode(root, 0).val;
};

var test = require('ava');
test('main', function(t) {
    var case1 = {
        val: 2,
        left: {
            val: 1
        },
        right: {
            val: 3
        }
    };
    t.is(findBottomLeftValue(case1), 1);
    var case2 = {
        val: 1,
        left: {
            val: 2,
            left: {
                val: 4
            }
        },
        right: {
            val: 3,
            left: {
                val: 5,
                left: {
                    val: 7
                }
            },
            right: {
                val: 6
            }
        }
    };
    t.is(findBottomLeftValue(case2), 7);
});
