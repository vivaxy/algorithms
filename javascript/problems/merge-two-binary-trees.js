/**
 * @since 2017-06-12 09:30:40
 * @author vivaxy
 *
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
var TreeNode = function(val) {
    this.val = val;
    this.left = this.right = null;
};
/**
 * @see https://leetcode.com/submissions/detail/106096147/
 *
 * @param {TreeNode} t1
 * @param {TreeNode} t2
 * @return {TreeNode}
 */
var mergeTrees = function(t1, t2) {
    var traverse = function(node1, node2) {
        var treeNode = null;
        if (!node1) {
            if (!node2) {
                return treeNode;
            }
            treeNode = new TreeNode(node2.val);
            treeNode.left = traverse(null, node2.left);
            treeNode.right = traverse(null, node2.right);
            return treeNode;
        }
        if (!node2) {
            treeNode = new TreeNode(node1.val);
            treeNode.left = traverse(node1.left, null);
            treeNode.right = traverse(node1.right, null);
            return treeNode;
        }
        treeNode = new TreeNode(node1.val + node2.val);
        treeNode.left = traverse(node1.left, node2.left);
        treeNode.right = traverse(node1.right, node2.right);
        return treeNode;
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
    var treeNode1 = new TreeNode(3);
    treeNode1.left = new TreeNode(4);
    treeNode1.right = new TreeNode(5);
    treeNode1.left.left = new TreeNode(5);
    treeNode1.left.right = new TreeNode(4);
    treeNode1.right.right = new TreeNode(7);
    t.deepEqual(mergeTrees(treeNode11, treeNode12), treeNode1);
});
