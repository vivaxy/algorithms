"""
https://leetcode.com/problems/valid-triangle-number/


"""


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(start, l, count):
            if len(l) == 3:
                if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]:
                    return 1
                return 0
            localCount = 0
            for i in range(start, len(nums)):
                localCount += dfs(i + 1, l + [nums[i]], count)
            return localCount
        return dfs(0, [], 0)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.triangleNumber([2, 2, 3, 4]), 3)


if __name__ == '__main__':
    unittest.main()
