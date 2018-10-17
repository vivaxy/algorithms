"""
https://leetcode.com/problems/escape-the-ghosts/

https://leetcode.com/submissions/detail/148753087/
"""


class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def distance(point, target):
            return abs(point[0] - target[0]) + abs(point[1] - target[1])
        meToTarget = distance(target, [0, 0])
        for ghost in ghosts:
            if distance(ghost, target) <= meToTarget:
                return False
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.escapeGhosts(
            [[1, 8], [-9, 0], [-7, -6], [4, 3], [1, 3]], [6, -9]), False)
        self.assertEqual(solution.escapeGhosts([[2, 0]], [1, 0]), False)
        self.assertEqual(solution.escapeGhosts([[1, 0]], [2, 0]), False)
        self.assertEqual(solution.escapeGhosts([[1, 0], [0, 3]], [0, 1]), True)
        self.assertEqual(solution.escapeGhosts(
            [[-1, 0], [0, 1], [-1, 0], [0, 1], [-1, 0]], [0, 0]), True)


if __name__ == '__main__':
    unittest.main()
