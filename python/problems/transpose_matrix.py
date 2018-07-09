"""
https://leetcode.com/problems/transpose-matrix/description/

https://leetcode.com/submissions/detail/162828786/
"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        rowCount = len(A)
        colCount = len(A[0])
        for colIndex in range(colCount):
            row = []
            for rowIndex in range(rowCount):
                row.append(A[rowIndex][colIndex])
            ans.append(row)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [
                         [1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(solution.transpose(
            [[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])


if __name__ == '__main__':
    unittest.main()
