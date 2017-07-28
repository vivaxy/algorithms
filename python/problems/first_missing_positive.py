"""
https://leetcode.com/problems/first-missing-positive/

https://leetcode.com/submissions/detail/111505702/
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = 1
        while missing in nums:
            missing += 1
        return missing


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.firstMissingPositive([1, 2, 0]), 3)


if __name__ == '__main__':
    unittest.main()
