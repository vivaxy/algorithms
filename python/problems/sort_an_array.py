"""
https://leetcode.com/problems/sort-an-array/

https://leetcode.com/submissions/detail/224682134/
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.sortArray([5, 2, 3, 1]), [1, 2, 3, 5])
        self.assertEqual(solution.sortArray(
            [5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])


if __name__ == '__main__':
    unittest.main()
