"""
https://leetcode.com/problems/find-the-duplicate-number/

https://leetcode.com/submissions/detail/111366012/
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)
        for prev, next in zip(sortedNums, sortedNums[1:]):
            print(prev, next)
            if prev == next:
                return prev


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findDuplicate([1, 2, 2, 3]), 2)
        self.assertEqual(solution.findDuplicate([2, 1, 2]), 2)


if __name__ == '__main__':
    unittest.main()
