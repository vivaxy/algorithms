"""
https://leetcode.com/problems/spiral-matrix-iii/

https://leetcode.com/submissions/detail/178784709/
"""


class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        direction = 0  # 0 ->
        sl = 1
        csl = sl
        cur = [r0, c0]
        ans = [cur]
        while len(ans) < R * C:
            if direction == 0:
                cur = [cur[0], cur[1] + 1]
            elif direction == 1:
                cur = [cur[0] + 1, cur[1]]
            elif direction == 2:
                cur = [cur[0], cur[1] - 1]
            elif direction == 3:
                cur = [cur[0] - 1, cur[1]]
            if cur[0] >= 0 and cur[0] < R and cur[1] >= 0 and cur[1] < C:
                ans.append(cur)
            csl -= 1

            if csl == 0:
                # change direction
                if direction == 0:
                    csl = sl
                    direction = 1
                elif direction == 1:
                    sl += 1
                    csl = sl
                    direction = 2
                elif direction == 2:
                    csl = sl
                    direction = 3
                elif direction == 3:
                    sl += 1
                    csl = sl
                    direction = 0
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.spiralMatrixIII(1, 4, 0, 0),
                         [[0, 0], [0, 1], [0, 2], [0, 3]])
        self.assertEqual(solution.spiralMatrixIII(5, 6, 1, 4), [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [
                         3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]])


if __name__ == '__main__':
    unittest.main()
