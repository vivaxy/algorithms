"""
https://leetcode.com/problems/sort-array-by-parity-ii/description/

https://leetcode.com/submissions/detail/183073832/
"""


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):
            if i % 2 == A[i] % 2:
                continue
            j = i + 1
            while A[j] % 2 != i % 2:
                j += 1
            A[i], A[j] = A[j], A[i]
        return A


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.sortArrayByParityII([4, 2, 5, 7]), [4, 5, 2, 7])
        self.assertEqual(solution.sortArrayByParityII([3, 1, 4, 2]), [4, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
