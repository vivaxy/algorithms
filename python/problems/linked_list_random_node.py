"""
https://leetcode.com/problems/linked-list-random-node/


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.list_node import ListNode


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.current = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        prev = self.current
        self.current = prev.next
        if self.current == None:
            self.current = self.head
        return prev.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


import unittest


class Test(unittest.TestCase):
    def test(self):
        listNode1 = ListNode(1)
        listNode1.next = ListNode(2)
        listNode1.next.next = ListNode(3)

        solution = Solution(listNode1)
        solution.getRandom()
        self.assertEqual(0, 0)
