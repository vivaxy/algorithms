/**
 * @since 2017-05-31 10:42:50
 * @author vivaxy
 * @see https://leetcode.com/problems/convert-bst-to-greater-tree/

 Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

 Example:

 Input: The root of a Binary Search Tree like this:
 5
 /   \
 2     13

 Output: The root of a Greater Tree like this:
 18
 /   \
 20     13

 */

/**
 * @see https://leetcode.com/submissions/detail/104705120/
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @typedef {Object} TreeNode
 * @property {number} val
 * @property {?TreeNode} left
 * @property {?TreeNode} right
 *
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var convertBST1 = function(root) {
    var allNodes = [];
    var traverse = function(node, callback) {
        callback(node.val, node);
        if (node.left) {
            traverse(node.left, callback);
        }
        if (node.right) {
            traverse(node.right, callback);
        }
    };
    if (root) {
        traverse(root, function(val) {
            allNodes.push(val);
        });
    }
    if (root) {
        traverse(root, function(val, node) {
            for (var i = 0; i < allNodes.length; i++) {
                if (allNodes[i] > val) {
                    node.val += allNodes[i];
                }
            }
        });
    }
    return root;
};

/**
 * @see https://leetcode.com/submissions/detail/104780858/
 * 深度优先，右子树优先，加上右侧的值
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @typedef {Object} TreeNode
 * @property {number} val
 * @property {?TreeNode} left
 * @property {?TreeNode} right
 *
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var convertBST2 = function(root) {
    var sum = 0;
    var traverse = function(node) {
        if (!node) {
            return;
        }
        traverse(node.right);
        sum += node.val;
        node.val = sum;
        traverse(node.left);
    };
    traverse(root);
    return root;
};

var test = require('ava');
test('convert-bst-to-greater-tree', function(t) {
    var input1 = {
        val: 5,
        left: {
            val: 2,
            left: null,
            right: null
        },
        right: {
            val: 13,
            left: null,
            right: null
        }
    };
    t.deepEqual(convertBST1(input1), {
        val: 18,
        left: {
            val: 20,
            left: null,
            right: null
        },
        right: {
            val: 13,
            left: null,
            right: null
        }
    });

    var input2 = {
        val: 5,
        left: {
            val: 2,
            left: null,
            right: null
        },
        right: {
            val: 13,
            left: null,
            right: null
        }
    };
    t.deepEqual(convertBST2(input2), {
        val: 18,
        left: {
            val: 20,
            left: null,
            right: null
        },
        right: {
            val: 13,
            left: null,
            right: null
        }
    });
});
