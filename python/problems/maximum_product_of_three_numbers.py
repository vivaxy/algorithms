"""
https://leetcode.com/problems/maximum-product-of-three-numbers/

https://leetcode.com/submissions/detail/111360714/
"""

import sys


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = sys.maxsize
        min2 = sys.maxsize
        max1 = -sys.maxsize
        max2 = -sys.maxsize
        max3 = -sys.maxsize
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, min1 * min2 * max1)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maximumProduct([1, 2, 3]), 6)
        self.assertEqual(solution.maximumProduct([-1, 2, 3]), -6)
        self.assertEqual(solution.maximumProduct([-1, -2, -3]), -6)
        self.assertEqual(solution.maximumProduct([-4, -3, -2, -1, 60]), 720)


if __name__ == '__main__':
    unittest.main()
