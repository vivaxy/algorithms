"""
https://leetcode.com/problems/available-captures-for-rook/


"""

from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rock = {'ri': -1, 'ci': -1}
        for ri in range(len(board)):
            if rock['ri'] != -1:
                break
            for ci in range(len(board[ri])):
                if board[ri][ci] == 'R':
                    rock['ri'] = ri
                    rock['ci'] = ci
                    break
        ans = 0
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rd, cd = direction
            ri = rock['ri'] + rd
            ci = rock['ci'] + cd
            while ri >= 0 and ri < len(board) and ci >= 0 and ci < len(board[ri]):
                if board[ri][ci] == 'B':
                    break
                if board[ri][ci] == 'p':
                    ans += 1
                    break
                ri += rd
                ci += cd
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numRookCaptures([
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", "R", ".", ".", ".", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]
        ]), 3)
        self.assertEqual(solution.numRookCaptures([
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "B", "R", "B", "p", ".", "."],
            [".", "p", "p", "B", "p", "p", ".", "."],
            [".", "p", "p", "p", "p", "p", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]
        ]), 0)
        self.assertEqual(solution.numRookCaptures([
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            ["p", "p", ".", "R", ".", "p", "B", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "B", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]
        ]), 3)


if __name__ == '__main__':
    unittest.main()
