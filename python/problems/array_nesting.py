"""
https://leetcode.com/problems/array-nesting/

https://leetcode.com/submissions/detail/107150941/
"""


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        calulatedSet = set()
        for i in range(len(nums)):
            indexSet = set()
            setLen = -1
            nextIndex = i
            if not i in calulatedSet:
                while len(indexSet) > setLen:
                    setLen = len(indexSet)
                    indexSet.add(nextIndex)
                    calulatedSet.add(nextIndex)
                    nextIndex = nums[nextIndex]
                if setLen > max:
                    max = setLen
        return max


import unittest


class Test(unittest.TestCase):
    def test(self):
        solition = Solution()
        self.assertEqual(solition.arrayNesting([5, 4, 0, 3, 1, 6, 2]), 4)


if __name__ == '__main__':
    unittest.main()
