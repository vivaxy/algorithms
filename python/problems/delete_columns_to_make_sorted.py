import unittest
from typing import List
"""
https://leetcode.com/problems/delete-columns-to-make-sorted/

https://leetcode.com/submissions/detail/213230105/
"""


class Solution:
    def minDeletionSize(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A[0])):
            max = 0
            for a in A:
                if ord(a[i]) >= max:
                    max = ord(a[i])
                    continue
                ans += 1
                break
        return ans


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minDeletionSize(["cba", "daf", "ghi"]), 1)
        self.assertEqual(solution.minDeletionSize(["a", "b"]), 0)
        self.assertEqual(solution.minDeletionSize(["zyx", "wvu", "tsr"]), 3)
        self.assertEqual(solution.minDeletionSize(["rrjk", "furt", "guzm"]), 2)


if __name__ == '__main__':
    unittest.main()
