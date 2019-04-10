"""
https://leetcode.com/problems/di-string-match/

https://leetcode.com/submissions/detail/214609509/
"""

from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans = []
        arr = list(range(0, len(S) + 1))
        for char in S:
            if char == 'D':
                ans.append(arr.pop())
            else:
                ans.append(arr.pop(0))
        ans.append(arr.pop())
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.diStringMatch('IDID'), [0, 4, 1, 3, 2])
        self.assertEqual(solution.diStringMatch('III'), [0, 1, 2, 3])
        self.assertEqual(solution.diStringMatch('DDI'), [3, 2, 0, 1])


if __name__ == '__main__':
    unittest.main()
