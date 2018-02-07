"""
https://leetcode.com/problems/linked-list-random-node/

https://leetcode.com/submissions/detail/139767568/
https://leetcode.com/submissions/detail/139768870/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.list_node import ListNode
import random


class Solution1(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        node = head
        while node:
            node = node.next
            self.length += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        index = random.randrange(0, self.length)
        node = self.head
        while index:
            node = node.next
            index -= 1
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        ans = self.head
        index = 1
        node = ans.next
        while node:
            value = random.randrange(0, index + 1)
            if value == 0:
                ans = node
            index += 1
            node = node.next
        return ans.val


import unittest


class Test(unittest.TestCase):
    def test(self):
        listNode1 = ListNode(1)
        solution = Solution(listNode1)
        self.assertEqual(solution.getRandom(), 1)


if __name__ == '__main__':
    unittest.test()
