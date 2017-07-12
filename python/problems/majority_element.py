"""
https://leetcode.com/problems/majority-element/

https://leetcode.com/submissions/detail/109296614/
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for value in nums:
            if not value in dic:
                dic[value] = 0
            dic[value] = dic.get(value) + 1
        for value in dic.keys():
            if dic[value] > len(nums) / 2:
                return value


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.majorityElement([1]), 1)
        self.assertEqual(solution.majorityElement([3, 2, 3]), 3)


if __name__ == '__main__':
    unittest.main()
