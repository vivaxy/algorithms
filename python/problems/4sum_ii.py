"""
https://leetcode.com/problems/4sum-ii/

https://leetcode.com/submissions/detail/139449882/
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = dict()
        count = 0
        for a in A:
            for b in B:
                s = a + b
                if s in dic:
                    dic[s] += 1
                else:
                    dic[s] = 1
        for c in C:
            for d in D:
                s = c + d
                if -s in dic:
                    count += dic[-s]
        return count


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.fourSumCount(
            [1, 2], [-2, -1], [-1, 2], [0, 2]), 2)


if __name__ == '__main__':
    unittest.main()
