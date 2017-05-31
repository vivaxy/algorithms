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
var convertBST = function(root) {

};

var test = require('ava');
test('convert-bst-to-greater-tree', function(t) {
    var input = {
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
    t.deepEqual(input, {
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
    });
});
