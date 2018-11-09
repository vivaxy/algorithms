"""
https://leetcode.com/problems/mirror-reflection/

https://leetcode.com/submissions/detail/188479582/
"""


class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        x0, y0 = 0, 0
        x1, y1 = p, q
        targets = [(p, 0), (p, p), (0, p)]
        while (x1, y1) not in targets:
            dy = y1 - y0
            x0 = x1
            y0 = y1
            if x1 == 0:
                # to the right
                x1 = p
            else:
                # to the left
                x1 = 0
            y1 = y0 + dy
            if y1 > p:
                y0 = p + p - y0
                y1 = p + p - y1
            elif y1 < 0:
                y0 = 0 - y0
                y1 = 0 - y1
        return targets.index((x1, y1))


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.mirrorReflection(2, 1), 2)
        self.assertEqual(solution.mirrorReflection(4, 3), 2)


if __name__ == '__main__':
    unittest.main()
