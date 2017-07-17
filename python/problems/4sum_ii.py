"""
https://leetcode.com/problems/4sum-ii/


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
        count = 0
        for a in A:
            for b in B:
                for c in C:
                    for d in D:
                        if a + b + c + d == 0:
                            count += 1
        return count


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.fourSumCount(
            [1, 2], [-2, -1], [-1, 2], [0, 2]), 2)


if __name__ == '__main__':
    unittest.main()
