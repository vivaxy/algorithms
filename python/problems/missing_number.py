"""
https://leetcode.com/problems/missing-number/

https://leetcode.com/submissions/detail/111365539/
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) + 1) * len(nums) / 2 - sum(nums)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([0, 1, 3]), 2)
        self.assertEqual(solution.missingNumber([0]), 1)
        self.assertEqual(solution.missingNumber([1]), 0)
        self.assertEqual(solution.missingNumber([2, 0]), 1)


if __name__ == '__main__':
    unittest.main()
