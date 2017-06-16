/**
 * @since 2017-06-07 10:22:44
 * @author vivaxy
 *
 * @see https://leetcode.com/problems/construct-string-from-binary-tree/

 You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

 The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

 Example 1:
 Input: Binary tree: [1,2,3,4]
 1
 /   \
 2     3
 /
 4

 Output: "1(2(4))(3)"

 Explanation: Originallay it needs to be "1(2(4)())(3()())",
 but you need to omit all the unnecessary empty parenthesis pairs.
 And it will be "1(2(4))(3)".
 Example 2:
 Input: Binary tree: [1,2,3,null,4]
 1
 /   \
 2     3
 \
 4

 Output: "1(2()(4))(3)"

 Explanation: Almost the same as the first example,
 except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @see https://leetcode.com/submissions/detail/105216714/
 *
 * @typedef {Object} TreeNode
 * @property {number} val
 * @property {?TreeNode} left
 * @property {?TreeNode} right
 *
 * @param {TreeNode} t
 * @return {string}
 */
var tree2str = function(t) {
    var traverse = function(node) {
        if (!node) {
            return '';
        }
        var leftContent = traverse(node.left);
        var rightContent = traverse(node.right);
        if (rightContent) {
            return String(node.val) + '(' + leftContent + ')(' + rightContent + ')';
        }
        if (leftContent) {
            return String(node.val) + '(' + leftContent + ')';
        }
        return String(node.val);
    };
    return traverse(t);
};

var test = require('ava');
test('main', function(t) {
    var tree1 = {
        val: 1,
        left: {
            val: 2,
            left: {
                val: 4
            }
        },
        right: {
            val: 3
        }
    };
    t.is(tree2str(tree1), '1(2(4))(3)');
    var tree2 = {
        val: 1,
        left: {
            val: 2,
            right: {
                val: 4
            }
        },
        right: {
            val: 3
        }
    };
    t.is(tree2str(tree2), '1(2()(4))(3)');
});
