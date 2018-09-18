"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/


"""


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = A[0]
        for i in range(1, len(A)):
            if A[i] > m:
                m = A[i]
            else:
                return i - 1


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.peakIndexInMountainArray([0,1,0]), 1)
        self.assertEqual(solution.peakIndexInMountainArray([0,2,1,0]), 1)


if __name__ == '__main__':
    unittest.main()
