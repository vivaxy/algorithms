"""
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/


"""


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for digits in range(31, 0, -1):
            pass
        return 0


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findMaximumXOR([]), 0)


if __name__ == '__main__':
    unittest.main()
