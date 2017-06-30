"""
https://leetcode.com/problems/assign-cookies/

https://leetcode.com/submissions/detail/107830080/
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        contented = 0
        g = sorted(g)
        s = sorted(s)
        cookieIndex = 0
        for child in g:
            while cookieIndex < len(s) and child > s[cookieIndex]:
                cookieIndex += 1
            if cookieIndex >= len(s):
                break
            else:
                contented += 1
                cookieIndex += 1
        return contented

import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findContentChildren([1, 2, 3], [1, 1]), 1)
        self.assertEqual(solution.findContentChildren([1, 2], [1, 2, 3]), 2)


if __name__ == '__main__':
    unittest.main()
