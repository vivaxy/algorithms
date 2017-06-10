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
/**
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
            return {
                val: nums[start],
                left: null,
                right: null
            };
        }
        var mid = Math.floor((start + end) / 2);
        return {
            val: nums[mid],
            left: traverse(start, mid - 1),
            right: traverse(mid + 1, end)
        };
    };
    return traverse(0, nums.length - 1);
};

var test = require('ava');
test('main', function(t) {
    var treeNode = {
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
            val: 6,
            left: {
                val: 5,
                left: null,
                right: null
            },
            right: {
                val: 7,
                left: null,
                right: null
            }
        }
    };
    t.deepEqual(sortedArrayToBST([1, 2, 3, 4, 5, 6, 7]), treeNode);
    t.deepEqual(sortedArrayToBST([]), null);
    var treeNode2 = {
        val: 1,
        left: null,
        right: {
            val: 3,
            left: null,
            right: null
        }
    };
    t.deepEqual(sortedArrayToBST([1, 3]), treeNode2);
    var treeNode3 = {
        val: 0,
        left: null,
        right: null
    };
    t.deepEqual(sortedArrayToBST([0]), treeNode3);
});
