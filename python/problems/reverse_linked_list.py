"""
https://leetcode.com/problems/reverse-linked-list/

https://leetcode.com/submissions/detail/141140132/
"""

from common.list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = None
        nextNode = head
        while nextNode:
            newNextHead = ListNode(nextNode.val)
            if ans:
                newNextHead.next = ans
            ans = newNextHead
            nextNode = nextNode.next
        return ans


import unittest
from common.assert_list_node_equal import assertListNodeEqual


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        listNode1 = ListNode(1)
        listNode1.next = ListNode(2)
        listNode1r = ListNode(2)
        listNode1r.next = ListNode(1)
        self.assertEqual(assertListNodeEqual(
            solution.reverseList(listNode1), listNode1r), True)


if __name__ == '__main__':
    unittest.main()
