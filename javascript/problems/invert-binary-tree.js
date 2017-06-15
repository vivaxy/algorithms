/**
 * @since 2017-06-15 10:49:10
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/invert-binary-tree/

 Invert a binary tree.

 4
 /   \
 2     7
 / \   / \
 1   3 6   9
 to
 4
 /   \
 7     2
 / \   / \
 9   6 3   1

 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @see https://leetcode.com/submissions/detail/106097034/
 *
 * @param {?TreeNode} root
 * @return {?TreeNode}
 */
var invertTree = function(root) {
    if (!root) {
        return null;
    }
    var temp = root.left;
    root.left = root.right;
    root.right = temp;
    invertTree(root.left);
    invertTree(root.right);
    return root;
};

var test = require('ava');
test('main', function(t) {
    var treeNode1 = {
        val: 4,
        left: {
            val: 2,
            left: {
                val: 1,
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
            val: 7,
            left: {
                val: 6,
                left: null,
                right: null
            },
            right: {
                val: 9,
                left: null,
                right: null
            }
        }
    };

    var treeNode1Result = {
        val: 4,
        left: {
            val: 7,
            left: {
                val: 9,
                left: null,
                right: null
            },
            right: {
                val: 6,
                left: null,
                right: null
            }
        },
        right: {
            val: 2,
            left: {
                val: 3,
                left: null,
                right: null
            },
            right: {
                val: 1,
                left: null,
                right: null
            }
        }
    };
    t.deepEqual(invertTree(treeNode1), treeNode1Result);
});
