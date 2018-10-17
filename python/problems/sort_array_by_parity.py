"""
https://leetcode.com/problems/sort-array-by-parity/

https://leetcode.com/submissions/detail/176526312/
"""


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        while i < j:
            while i < j and A[i] % 2 == 0:
                i += 1
            while i < j and A[j] % 2 == 1:
                j -= 1
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A




import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.sortArrayByParity([3, 1, 2, 4]), [4, 2, 1, 3])
        self.assertEqual(solution.sortArrayByParity([0, 2]), [0, 2])


if __name__ == '__main__':
    unittest.main()
