"""
https://leetcode.com/problems/find-common-characters/

https://leetcode.com/submissions/detail/215127668/
"""

from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = list(A[0])
        for word in A[1:]:
            ci = 0
            while ci < len(ans):
                char = ans[ci]
                if char in word:
                    i = word.find(char)
                    word = word[:i] + word[i + 1:]
                    ci += 1
                else:
                    ans.remove(char)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.commonChars(
            ["bella", "label", "roller"]), ["e", "l", "l"])
        self.assertEqual(solution.commonChars(
            ["cool", "lock", "cook"]), ["c", "o"])
        self.assertEqual(solution.commonChars(
            ["daaccccd", "adacbdda", "abddbaba", "bacbcbcb",
                "bdaaaddc", "cdadacba", "bacbdcda", "bacdaacd"]
        ), ["a"])


if __name__ == '__main__':
    unittest.main()
