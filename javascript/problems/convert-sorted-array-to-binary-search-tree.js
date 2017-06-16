/**
 * @since 2017-06-10 13:54:06
 * @author vivaxy
 * @see https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

 Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

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
 * @see https://leetcode.com/submissions/detail/106203322/
 *
 * @param {number[]} nums
 * @return {?TreeNode}
 */
var sortedArrayToBST = function(nums) {
    if (nums.length === 0) {
        return null;
    }
    var traverse = function(start, end) {
        if (start > end) {
            return null;
        }
        if (start === end) {
            return new TreeNode(nums[start]);
        }
        var mid = Math.floor((start + end) / 2);
        var treeNode = new TreeNode(nums[mid]);
        treeNode.left = traverse(start, mid - 1);
        treeNode.right = traverse(mid + 1, end);
        return treeNode;
    };
    return traverse(0, nums.length - 1);
};

var test = require('ava');
test('main', function(t) {
    var treeNode1 = new TreeNode(4);
    treeNode1.left = new TreeNode(2);
    treeNode1.left.left = new TreeNode(1);
    treeNode1.left.right = new TreeNode(3);
    treeNode1.right = new TreeNode(6);
    treeNode1.right.left = new TreeNode(5);
    treeNode1.right.right = new TreeNode(7);
    t.deepEqual(sortedArrayToBST([1, 2, 3, 4, 5, 6, 7]), treeNode1);

    t.deepEqual(sortedArrayToBST([]), null);

    var treeNode2 = new TreeNode(1);
    treeNode2.right = new TreeNode(3);
    t.deepEqual(sortedArrayToBST([1, 3]), treeNode2);

    var treeNode3 = new TreeNode(0);
    t.deepEqual(sortedArrayToBST([0]), treeNode3);
});
