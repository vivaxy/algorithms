/**
 * @since 2017-06-10 15:37:43
 * @author vivaxy
 * @see https://leetcode.com/problems/remove-linked-list-elements/

 Remove all elements from a linked list of integers that have value val.

 Example
 Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
 Return: 1 --> 2 --> 3 --> 4 --> 5

 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @see https://leetcode.com/submissions/detail/105563621/
 *
 * @typedef {Object} ListNode
 * @property {number} val
 * @property {?ListNode} next
 *
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    var traverse = function(node, prev) {
        if (!node) {
            return;
        }
        if (node.val === val) {
            if (prev) {
                prev.next = node.next;
                traverse(node.next, prev);
            } else {
                head = node.next;
                traverse(head, null);
            }
        } else {
            traverse(node.next, node);
        }
    };
    traverse(head, null);
    return head;
};

var test = require('ava');
test('main', function(t) {
    var listNode = {
        val: 1,
        next: {
            val: 2,
            next: {
                val: 3,
                next: {
                    val: 4,
                    next: {
                        val: 5,
                        next: null
                    }
                }
            }
        }
    };
    var resultListNode = {
        val: 1,
        next: {
            val: 2,
            next: {
                val: 3,
                next: {
                    val: 5,
                    next: null
                }
            }
        }
    };
    t.deepEqual(removeElements(listNode, 4), resultListNode);

    var listNode2 = {
        val: 1,
        next: {
            val: 2,
            next: {
                val: 6,
                next: {
                    val: 3,
                    next: {
                        val: 4,
                        next: {
                            val: 5,
                            next: {
                                val: 6,
                                next: null
                            }
                        }
                    }
                }
            }
        }
    };
    var resultListNode2 = {
        val: 1,
        next: {
            val: 2,
            next: {
                val: 3,
                next: {
                    val: 4,
                    next: {
                        val: 5,
                        next: null
                    }
                }
            }
        }
    };
    t.deepEqual(removeElements(listNode2, 6), resultListNode2);

    var listNode3 = {
        val: 1,
        next: null
    };
    var resultListNode3 = null;
    t.deepEqual(removeElements(listNode3, 1), resultListNode3);

    var listNode4 = {
        val: 1,
        next: {
            val: 1,
            next: null
        }
    };
    var resultListNode4 = null;
    t.deepEqual(removeElements(listNode4, 1), resultListNode4);


    var listNode5 = {
        val: 1,
        next: {
            val: 2,
            next: {
                val: 2,
                next: {
                    val: 1,
                    next: null
                }
            }
        }
    };
    var resultListNode5 = {
        val: 1,
        next: {
            val: 1,
            next: null
        }
    };
    t.deepEqual(removeElements(listNode5, 2), resultListNode5);

});
