"""
https://leetcode.com/problems/contains-duplicate/

https://leetcode.com/submissions/detail/111359118/
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortedNum = sorted(nums)
        for prev, next in zip(sortedNum[1:], sortedNum[:len(sortedNum) - 1]):
            if prev == next:
                return True
        return False


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.containsDuplicate([1, 2, 3, 4, 5]), False)
        self.assertEqual(solution.containsDuplicate([1, 2, 2]), True)


if __name__ == '__main__':
    unittest.main()
