"""
https://leetcode.com/problems/permutations/

https://leetcode.com/submissions/detail/148835681/
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def p(got, toGet):
            if len(toGet) == 0:
                ans.append(got)
                return
            for i in toGet:
                nextToGet = toGet[:]
                nextToGet.remove(i)
                p(got + [i], nextToGet)
        p([], nums)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.permute([1, 2, 3]), [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ])


if __name__ == '__main__':
    unittest.main()
