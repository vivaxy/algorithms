"""
https://leetcode.com/problems/minimum-falling-path-sum/

https://leetcode.com/submissions/detail/186516905/
"""


class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        colCount = len(A[0])
        ans = [0] * colCount
        for rowIndex in range(len(A)):
            nextAns = []
            for colIndex in range(colCount):
                minCurValue = 101
                for diffIndex in [-1, 0, 1]:
                    prevColIndex = colIndex + diffIndex
                    if prevColIndex < 0 or prevColIndex >= colCount:
                        continue
                    minCurValue = min(minCurValue, ans[prevColIndex] + A[rowIndex][colIndex])
                nextAns.append(minCurValue)
            ans = nextAns
        return min(ans)



import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]), 12)


if __name__ == '__main__':
    unittest.main()
