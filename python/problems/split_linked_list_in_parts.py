"""
https://leetcode.com/problems/split-linked-list-in-parts/description/

https://leetcode.com/submissions/detail/144005053/
"""

from common.list_node import ListNode
from common.assert_list_node_array_equal import assertListNodeArrayEqual

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        count = 0
        node = root
        while node:
            count += 1
            node = node.next
        baseNodeLen = int(count / k)
        extraLenCount = count % k
        ans = []
        newRoot = root
        for index in range(k):
            if newRoot == None:
                ans.append(None)
                continue
            currentLen = baseNodeLen
            lastNode = newRoot
            if extraLenCount > 0:
                currentLen += 1
                extraLenCount -= 1
            for i in range(currentLen - 1):
                lastNode = lastNode.next
            currentRoot = newRoot
            newRoot = lastNode.next
            lastNode.next = None
            ans.append(currentRoot)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        listNode1 = ListNode(1)
        listNode1.next = ListNode(2)
        listNode1.next.next = ListNode(3)
        listNode11 = ListNode(1)
        listNode12 = ListNode(2)
        listNode13 = ListNode(3)
        self.assertEqual(assertListNodeArrayEqual(solution.splitListToParts(
            listNode1, 5), [listNode11, listNode12, listNode13, None, None]), True)
        listNode2 = ListNode(1)
        listNode2.next = ListNode(2)
        listNode2.next.next = ListNode(3)
        listNode2.next.next.next = ListNode(4)
        listNode2.next.next.next.next = ListNode(5)
        listNode2.next.next.next.next.next = ListNode(6)
        listNode2.next.next.next.next.next.next = ListNode(7)
        listNode2.next.next.next.next.next.next.next = ListNode(8)
        listNode2.next.next.next.next.next.next.next.next = ListNode(9)
        listNode2.next.next.next.next.next.next.next.next.next = ListNode(10)
        listNode21 = ListNode(1)
        listNode21.next = ListNode(2)
        listNode21.next.next = ListNode(3)
        listNode21.next.next.next = ListNode(4)
        listNode22 = ListNode(5)
        listNode22.next = ListNode(6)
        listNode22.next.next = ListNode(7)
        listNode23 = ListNode(8)
        listNode23.next = ListNode(9)
        listNode23.next.next = ListNode(10)
        self.assertEqual(assertListNodeArrayEqual(solution.splitListToParts(
            listNode2, 3), [listNode21, listNode22, listNode23]), True)
        self.assertEqual(assertListNodeArrayEqual(
            solution.splitListToParts(None, 3), [None, None, None]), True)


if __name__ == '__main__':
    unittest.main()
