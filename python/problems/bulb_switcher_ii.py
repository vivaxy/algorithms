"""
https://leetcode.com/problems/bulb-switcher-ii/description/

https://leetcode.com/submissions/detail/140962396/
"""


class Solution1:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        def flipEvery(x, index):
            return not x

        def flipEven(x, index):
            if index % 2 == 1:
                return x
            return not x

        def flipOdd(x, index):
            if index % 2 == 1:
                return not x
            return x

        def flip3k1(x, index):
            if (index - 1) % 3 == 0:
                return not x
            return x
        status = set()
        actions = [flipEvery, flipEven, flipOdd, flip3k1]

        def stringifyLights(lights):
            st = ''
            for light in lights:
                if light:
                    st += '1'
                else:
                    st += '0'
            return st

        def flipLights(actions):
            lights = [True] * n
            for action in actions:
                lights = list(
                    map(action, lights, list(range(1, len(lights) + 1))))
            status.add(stringifyLights(lights))

        def traverse(steps):
            if len(steps) == m:
                return flipLights(steps)
            for action in actions:
                traverse(steps + [action])
        traverse([])
        return len(status)


class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            if m == 1:
                return 3
            return 4
        if m == 1:
            return 4
        if m == 2:
            return 7
        return 8


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.flipLights(3, 1), 4)
        self.assertEqual(solution.flipLights(2, 1), 3)
        self.assertEqual(solution.flipLights(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
