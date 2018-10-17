"""
https://leetcode.com/problems/flipping-an-image/

https://leetcode.com/submissions/detail/176060521/
"""


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for row in A:
            ansRow = []
            for i in range(len(row)):
                ansRow.append(1 - row[len(row) - i - 1])
            ans.append(ansRow)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]), [[1,0,0],[0,1,0],[1,1,1]])
        self.assertEqual(solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]), [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]])


if __name__ == '__main__':
    unittest.main()
