"""
https://leetcode.com/problems/friend-circles/

https://leetcode.com/submissions/detail/107341493/
"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        circles = 0
        students = list(range(len(M)))
        while len(students) > 0:
            circles += 1
            one = students[0]
            students.remove(one)
            group = [one]
            while len(group) > 0:
                current = group[0]
                i = 0
                while i < len(students):
                    st = students[i]
                    if st != current:
                        if M[st][current] == 1:
                            students.remove(st)
                            if not st in group:
                                group.append(st)
                        else:
                            i += 1
                group.remove(current)
        return circles


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findCircleNum(
            [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
        self.assertEqual(solution.findCircleNum(
            [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
        self.assertEqual(solution.findCircleNum(
            [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]), 1)
        self.assertEqual(solution.findCircleNum(
            [[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]), 1)


if __name__ == '__main__':
    unittest.main()
