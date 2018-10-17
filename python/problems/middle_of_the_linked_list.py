"""
https://leetcode.com/problems/middle-of-the-linked-list/

https://leetcode.com/submissions/detail/177596232/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common.list_node import ListNode
from common.list_to_list_node import listToListNode
from common.list_node_to_list import listNodeToList


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = head
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            if cnt == 2:
                ans = ans.next
                cnt = 0
            cur = cur.next
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(listNodeToList(solution.middleNode(
            listToListNode([1, 2, 3, 4, 5]))), [3, 4, 5])
        self.assertEqual(listNodeToList(solution.middleNode(
            listToListNode([1, 2, 3, 4, 5, 6]))), [4, 5, 6])


if __name__ == '__main__':
    unittest.main()
