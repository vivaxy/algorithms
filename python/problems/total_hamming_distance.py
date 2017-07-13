"""
https://leetcode.com/problems/total-hamming-distance/

https://leetcode.com/submissions/detail/109423341/
"""


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def traverse(array, sum):
            needLoop = False
            zeroCount = 0
            oneCount = 0
            current = 0
            for index, num in enumerate(array):
                remaining = num % 2
                if remaining == 0:
                    zeroCount += 1
                else:
                    oneCount += 1
                nextNum = (num - remaining) / 2
                if nextNum != 0:
                    needLoop = True
                array[index] = nextNum
                current = zeroCount * oneCount
            if needLoop:
                return current + traverse(array, sum)
            return current
        return traverse(nums, 0)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.totalHammingDistance([4, 14, 2]), 6)


if __name__ == '__main__':
    unittest.main()
