"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

https://leetcode.com/submissions/detail/111580779/
"""

import sys


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNumber = sys.maxsize
        maxNumber = -sys.maxsize
        maxFlag = False
        minFlag = False
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                minFlag = True
            if minFlag:
                minNumber = min(minNumber, nums[i + 1])
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                maxFlag = True
            if maxFlag:
                maxNumber = max(maxNumber, nums[i])
        for start in range(0, len(nums)):
            if minNumber < nums[start]:
                break
        for end in range(len(nums) - 1, -1, -1):
            if maxNumber > nums[end]:
                break
        if start >= end:
            return 0
        return end - start + 1


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findUnsortedSubarray(
            [2, 6, 4, 8, 10, 9, 15]), 5)
        self.assertEqual(solution.findUnsortedSubarray([1, 3, 2, 4, 5]), 2)
        self.assertEqual(solution.findUnsortedSubarray([1]), 0)


if __name__ == '__main__':
    unittest.main()
