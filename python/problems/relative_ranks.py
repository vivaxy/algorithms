"""
https://leetcode.com/problems/relative-ranks/

https://leetcode.com/submissions/detail/108769702/
"""


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortedNums = sorted(nums)[::-1]
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + list(map(str, range(4, len(nums) + 1)))
        zippedNums = zip(sortedNums, ranks)
        dicted = dict(zippedNums)
        return list(map(dicted.get, nums))


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findRelativeRanks(
            [5, 4, 3, 2, 1]),
            ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
        )


if __name__ == '__main__':
    unittest.main()
