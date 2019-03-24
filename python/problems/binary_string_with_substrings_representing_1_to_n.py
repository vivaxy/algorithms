"""
https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

https://leetcode.com/submissions/detail/217341263/
"""


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            s = bin(i)[2:]
            if s not in S:
                return False
        return True


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.queryString('0110', 3), True)
        self.assertEqual(solution.queryString('0110', 4), False)


if __name__ == '__main__':
    unittest.main()
