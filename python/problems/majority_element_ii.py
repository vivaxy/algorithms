"""
https://leetcode.com/problems/majority-element-ii/

https://leetcode.com/submissions/detail/111508134/
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = dict()
        for value in nums:
            if not value in dic:
                dic[value] = 0
            dic[value] = dic.get(value) + 1
        results = []
        for value in dic.keys():
            if dic[value] > len(nums) / 3:
                results.append(value)
        return results


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.majorityElement([1, 1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
