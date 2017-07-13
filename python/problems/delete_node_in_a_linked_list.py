"""
https://leetcode.com/problems/delete-node-in-a-linked-list/

https://leetcode.com/submissions/detail/109553590/
"""

from common.list_node import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        listNode1 = ListNode(1)
        listNode1.next = ListNode(2)
        currentNode1 = ListNode(3)
        listNode1.next.next = currentNode1
        listNode1.next.next.next = ListNode(4)
        solution.deleteNode(currentNode1)
        self.assertEqual(listNode1.next.next.val, 4)


if __name__ == '__main__':
    unittest.main()
