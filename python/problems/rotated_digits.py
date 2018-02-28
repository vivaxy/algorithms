"""
https://leetcode.com/problems/rotated-digits/description/

https://leetcode.com/submissions/detail/142723550/
"""


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        array = [2, 5, 6, 9]
        invalidArray = [3, 4, 7]
        ans = 0
        for i in range(1, N + 1):
            found = False
            for a in array:
                if str(i).find(str(a)) != -1:
                    found = True
            for a in invalidArray:
                if str(i).find(str(a)) != -1:
                    found = False
            if found:
                ans += 1
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.rotatedDigits(19), 8)
        self.assertEqual(solution.rotatedDigits(857), 247)
        self.assertEqual(solution.rotatedDigits(10), 4)


if __name__ == '__main__':
    unittest.main()
