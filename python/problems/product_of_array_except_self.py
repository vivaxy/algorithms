"""
https://leetcode.com/problems/product-of-array-except-self/

https://leetcode.com/submissions/detail/107507922/
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        temp = 1
        for i in range(0, n):
            result.append(temp)
            temp *= nums[i]
        temp = 1
        for i in range(n - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([]), [])


if __name__ == '__main__':
    unittest.main()
