"""
https://leetcode.com/problems/rotate-string/

https://leetcode.com/submissions/detail/145178981/
"""


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        length = len(A)
        while length:
            A = A[1:] + A[0:1]
            if A == B:
                return True
            length -= 1
        return False


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.rotateString('abcde', 'cdeab'), True)
        self.assertEqual(solution.rotateString('abcde', 'abced'), False)


if __name__ == '__main__':
    unittest.main()
