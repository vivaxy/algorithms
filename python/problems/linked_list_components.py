"""
https://leetcode.com/problems/linked-list-components/

https://leetcode.com/submissions/detail/190437499/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.list_to_list_node import listToListNode


class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        ans = 0
        s = set(G)

        prevNodeInS = False
        node = head
        while node:
            if node.val in s:
                if not prevNodeInS:
                    ans += 1
                prevNodeInS = True
            else:
                prevNodeInS = False
            node = node.next
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numComponents(
            listToListNode([0, 1, 2, 3]), [0, 1, 3]), 2)
        self.assertEqual(solution.numComponents(
            listToListNode([0, 1, 2, 3, 4]), [0, 3, 1, 4]), 2)


if __name__ == '__main__':
    unittest.main()
