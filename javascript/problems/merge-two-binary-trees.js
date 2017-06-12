/**
 * @since 2017-06-12 09:30:40
 * @author vivaxy
 * @see https://leetcode.com/problems/merge-two-binary-trees/

 Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

 You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

 Example 1:
 Input:
 Tree 1                     Tree 2
 1                         2
 / \                       / \
 3   2                     1   3
 /                           \   \
 5                             4   7
 Output:
 Merged tree:
 3
 / \
 4   5
 / \   \
 5   4   7
 Note: The merging process must start from the root nodes of both trees.

 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} t1
 * @param {TreeNode} t2
 * @return {TreeNode}
 */
var mergeTrees = function(t1, t2) {
    var traverse = function(node1, node2) {
        if (!node1) {
            if (!node2) {
                return null;
            }
            return {
                val: node2.val,
                left: traverse(null, node2.left),
                right: traverse(null, node2.right)
            };
        }
        if (!node2) {
            return {
                val: node1.val,
                left: traverse(node1.left, null),
                right: traverse(node1.right, null)
            };
        }
        return {
            val: node1.val + node2.val,
            left: traverse(node1.left, node2.left),
            right: traverse(node1.right, node2.right)
        };
    };
    return traverse(t1, t2);
};

var test = require('ava');
test('main', function(t) {
    var treeNode11 = {
        val: 1,
        left: {
            val: 3,
            left: {
                val: 5,
                left: null,
                right: null
            },
            right: null
        },
        right: {
            val: 2,
            left: null,
            right: null
        }
    };
    var treeNode12 = {
        val: 2,
        left: {
            val: 1,
            left: null,
            right: {
                val: 4,
                left: null,
                right: null
            }
        },
        right: {
            val: 3,
            left: null,
            right: {
                val: 7,
                left: null,
                right: null
            }
        }
    };
    var treeNode1 = {
        val: 3,
        left: {
            val: 4,
            left: {
                val: 5,
                left: null,
                right: null
            },
            right: {
                val: 4,
                left: null,
                right: null
            }
        },
        right: {
            val: 5,
            left: null,
            right: {
                val: 7,
                left: null,
                right: null
            }
        }
    };
    t.deepEqual(mergeTrees(treeNode11, treeNode12), treeNode1);
});
